import asyncio
import unittest
import time
# TODO: is to fix this parent-path
import sys
sys.path.append('..')
#
import Extentions.ini_deserializer as ini
import Extentions.json_serializer as json
import configparser
from unittest.mock import MagicMock, patch

class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super().__call__(*args, **kwargs)

class Tests(unittest.TestCase):
    @patch('Extentions.json_serializer.JsonSerializer.serialize', new_callable=AsyncMock)
    def test_json(self, json_mock):
        data = ['testdata', 'testdata', 'testdata', 'testdata', 'testdata']
        start_time = time.time()
        loop = asyncio.get_event_loop()
        loop.run_until_complete
        loop.run_until_complete(json.JsonSerializer.serialize(data, 333))
        loop.close()
        json_mock.assert_called_with(data, 333)
        print("--- First test: %s seconds ---" % (time.time() - start_time))

    def test_ini(self):
        config = configparser.ConfigParser()
        f_name = str(sys.argv[0]).split('.')[0] + '_settings.ini'
        start_time = time.time()
        res = ini.IniDeserializer.deserialize(config, f_name)
        API = config['API']['url']
        print(API)
        self.assertEqual('https://kinopoiskapiunofficial.tech/api/v2.1/films/',API)
        print("--- Second test: %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    unittest.main()