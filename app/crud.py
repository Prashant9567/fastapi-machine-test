from app import models
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError



# CATEGORY CRUD


# Create Category
def create_category(db, data):
    existing = db.query(models.Category).filter(models.Category.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")
    try:
        category = models.Category(name=data.name)
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error while creating category")


# Get all Categories (Pagination)
def get_categories(db, skip=0, limit=10):
    return (
        db.query(models.Category)
        .order_by(models.Category.id)   
        .offset(skip)
        .limit(limit)
        .all()
    )

# Get Category by ID
def get_category(db, id):
    category = db.query(models.Category).filter(models.Category.id == id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


# Update Category
def update_category(db, id, data):
    category = db.query(models.Category).filter(models.Category.id == id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    try:
        category.name = data.name
        db.commit()
        db.refresh(category)
        return category

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error while updating category")


# Delete Category
def delete_category(db, id):
    category = db.query(models.Category).filter(models.Category.id == id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    try:
        db.delete(category)
        db.commit()
        return {"message": "Category deleted successfully"}

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error while deleting category")



# PRODUCT CRUD


# Create Product
def create_product(db, data):
    # Check category exists
    category = db.query(models.Category).filter(models.Category.id == data.category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    try:
        product = models.Product(**data.dict())
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error while creating product")


# Get all Products (Pagination)
def get_products(db, skip=0, limit=10):
    return db.query(models.Product).order_by(models.Product.id).offset(skip).limit(limit).all()


# Get Product by ID
def get_product(db, id):
    product = db.query(models.Product).filter(models.Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


# Update Product
def update_product(db, id, data):
    product = db.query(models.Product).filter(models.Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    category = db.query(models.Category).filter(models.Category.id == data.category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    try:
        product.name = data.name
        product.price = data.price
        product.category_id = data.category_id

        db.commit()
        db.refresh(product)
        return product

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error while updating product")


# Delete Product
def delete_product(db, id):
    product = db.query(models.Product).filter(models.Product.id == id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    try:
        db.delete(product)
        db.commit()
        return {"message": "Product deleted successfully"}

    except SQLAlchemyError:
        db.rollback()
        raise HTTPException(status_code=500, detail="Database error while deleting product")