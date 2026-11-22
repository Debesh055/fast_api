from pydantic import BaseModel

class ProductDto(BaseModel):
    id:int
    title:str
    price:int|None=None
    count:int|None=None

