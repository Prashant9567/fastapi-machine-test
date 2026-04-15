from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

#Category Table

class Category(Base):
    __tablename__="categories"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(200),nullable=False)

    #relationship
    products=relationship("Product",back_populates="category")


#Product Table
class Product(Base):
    __tablename__="products"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(200),nullable=False)
    price=Column(Integer,nullable=False)

    category_id=Column(Integer,ForeignKey("categories.id"))

    #relationship
    category=relationship("Category",back_populates="products")