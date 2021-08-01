from abc import ABCMeta, abstractclassmethod

class IParser(meta=ABCMeta):
    @abstractclassmethod
    async def get_content():
        raise NotImplementedError
    
    @abstractclassmethod
    async def download_page(url:str):
        raise NotImplementedError
