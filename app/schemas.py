from pydantic import BaseModel

#Category

class CategoryCreate(BaseModel):
    name:str

#Reponse
class CategoryOut(BaseModel):
    id:int
    name:str

    class Config:
        orm_mode=True

#Prodcut
# Request (Create / Update)
class ProductCreate(BaseModel):
    name: str
    price: int
    category_id: int


# Response
class ProductOut(BaseModel):
    id: int
    name: str
    price: int
    category: CategoryOut   # ⭐ include category details

    class Config:
        orm_mode = True