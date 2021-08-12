from Parser.parser import IParser
import asyncio
import aiohttp
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
from datetime import timedelta, datetime
import Extentions.json_serializer as jsonext
#TODO
from concurrent.futures.thread import ThreadPoolExecutor



HEADERS = {
	'user-agent': UserAgent().random,
	'X-API-KEY' : '6b8a390e-e487-43f1-a124-e3e20345c2c2',
	'Accept': '*/*'
}
API = 'https://kinopoiskapiunofficial.tech/api/v2.1/films/389'
URL = 'https://www.kinopoisk.ru/film/389'

class KinopoiskParser(IParser):
    def __init__(self):
        #logger
        logging.basicConfig(filename='parser.log', encoding='utf-8', level=logging.DEBUG, 
            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filemode='w')

        #temp options
        self.__chrome_options = Options()
        self.__chrome_options.add_argument("--headless")
    
    async def get_html(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=HEADERS) as resp:
                if resp.status == 200:
                    logging.info(f'Connect to api status: {resp.status}')
                    return await resp.json()
                else:
                    logging.error(f'Connection error, status: {resp.status}')

    #TODO redesign it
    async def __get_html_driver(self, url):
        async with webdriver.Chrome(ChromeDriverManager().install(), options=self.__chrome_options) as driver:
            driver.implicitly_wait(10)
            async with driver.get(url) as resp:
                return await resp

    async def parse(self):
        try:
            response = await self.get_html(API)
            driver = await self.__get_html_driver(URL)
            movie = await self.__get_content(driver)
        
            response['data'].update(movie)

            #serialize
            loop = asyncio.get_event_loop()
            loop.run_until_complete(await jsonext.JsonSerializer.serialize(response, 3899))
            loop.close()

        except Exception as exc:
            logging.error(exc)

    #TODO
    async def __get_content(html:webdriver) -> dict:
        pass

    def dispose(self, driver: webdriver):
        driver.close()
        driver.quit()
        driver.stop_client()
        logging.info('Chrome driver is closed, memory is cleared')

if __name__ == '__main__':
    # ps
    a  = KinopoiskParser()
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(a.parse())
    print("--- Result time: %s seconds ---" % (time.time() - start_time))  