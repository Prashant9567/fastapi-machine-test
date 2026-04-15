from fastapi import APIRouter, Depends,  status
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal

#Create router
router=APIRouter()


# Dependency to get DB session
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Category Routes

# Create Category
@router.post("/categories",response_model=schemas.CategoryOut,status_code=status.HTTP_201_CREATED)
def create_category(category:schemas.CategoryCreate,db:Session=Depends(get_db)):
    return crud.create_category(db,category)

# Get all Categories (Pagination)
@router.get("/categories",response_model=list[schemas.CategoryOut])
def get_categories(page:int = 1,db:Session=Depends(get_db)):
    limit=10
    skip=(page-1)*limit
    return crud.get_categories(db,skip,limit)

# Get Category by ID
@router.get("/categories/{id}",response_model=schemas.CategoryOut)
def get_category(id:int,db:Session=Depends(get_db)):
    return crud.get_category(db,id)

# Update Category
@router.put("/categories/{id}",response_model=schemas.CategoryOut)
def update_category(id:int,category:schemas.CategoryCreate,db:Session=Depends(get_db)):
    return crud.update_category(db,id,category)

# Delete Category
@router.delete("/categories/{id}",status_code=status.HTTP_200_OK)   
def delete_category(id:int,db:Session=Depends(get_db)):
    return crud.delete_category(db,id)


#Product Routes

# Create Product
@router.post("/products",response_model=schemas.ProductOut,status_code=status.HTTP_201_CREATED)
def create_product(product:schemas.ProductCreate,db:Session=Depends(get_db)):
    return crud.create_product(db,product)

# Get all Products (Pagination)
@router.get("/products",response_model=list[schemas.ProductOut])
def get_products(page:int = 1,db:Session=Depends(get_db)):
    limit=10
    skip=(page-1)*limit
    return crud.get_products(db,skip,limit)

# Get Product by ID
@router.get("/products/{id}",response_model=schemas.ProductOut) 
def get_product(id:int,db:Session=Depends(get_db)):
    return crud.get_product(db,id)

# Update Product
@router.put("/products/{id}",response_model=schemas.ProductOut) 
def update_product(id:int,product:schemas.ProductCreate,db:Session=Depends(get_db)):
    return crud.update_product(db,id,product)

# Delete Product
@router.delete("/products/{id}",status_code=status.HTTP_200_OK)   
def delete_product(id:int,db:Session=Depends(get_db)):
    return crud.delete_product(db,id)