Project Overview
This project is a REST API built using FastAPI, MySQL, and SQLAlchemy ORM.
It provides CRUD operations for Category and Product with pagination and relationship handling.

Installation Steps

1. Create Virtual Environment
python -m venv venv

2. Activate Virtual Environment
Windows
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt
pip freeze

4. Environment Setup
Create a .env file in the root directory and add:
DATABASE_URL=mysql+pymysql://root:your_password@localhost:3306/fastapi-machine

5. Server Startup Command
Run the FastAPI application:
    uvicorn app.main:app --reload
API Documentation
 1. Swagger UI:
   http://127.0.0.1:8000/docs
 2.Postman

6. Steps to Run the Application
    Activate virtual environment
    Ensure MySQL server is running
    Create database machine
    Configure .env file
    Run server using uvicorn
    Open Swagger UI or Postman and test APIs

7. API Endpoints
    1. Category APIs
        POST /api/categories
        GET /api/categories?page=1
        GET /api/categories/{id}
        PUT /api/categories/{id}
        DELETE /api/categories/{id}
    2. Product APIs
        POST /api/products
        GET /api/products?page=1
        GET /api/products/{id}
        PUT /api/products/{id}
        DELETE /api/products/{id}


8. Database Design Details
    Categories Table
        id (Primary Key)
        name (Unique)
    Products Table
        id (Primary Key)
        name
        price
        category_id (Foreign Key)
9. Relationship
        One Category → Many Products
        One Product → One Category