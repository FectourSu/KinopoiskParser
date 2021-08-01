import asyncio
import configparser
import sys
import os
import errno
import asyncio

class SettingsDeserializer():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.f_name = str(sys.argv[0]).split('.')[0] + '_settings.ini'

    async def __deserialize(self):
        try:
            if os.path.exists(self.f_name) == False:
                await asyncio.sleep(0)
                open(self.f_name, "w").close
            await asyncio.sleep(0)
            self.config.read(self.f_name)
        except OSError as exc: 
            print(exc)
            if exc.errno != errno.EEXIST:
                raise

if __name__ == '__main__':
	config = SettingsDeserializer()
    api = config.config['API']