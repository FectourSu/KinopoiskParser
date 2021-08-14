from abc import ABCMeta, abstractclassmethod

class IParser():
    @abstractclassmethod
    async def parse(id:int):
        raise NotImplementedError
        
    @abstractclassmethod
    async def get_html(url:str):
        raise NotImplementedError