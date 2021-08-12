from abc import ABCMeta, abstractclassmethod

class IParser():
    @abstractclassmethod
    async def parse():
        raise NotImplementedError
        
    @abstractclassmethod
    async def get_html(url:str):
        raise NotImplementedError