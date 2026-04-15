# 🚀 FastAPI Machine Test

This is a robust REST API built with *FastAPI, **MySQL, and **SQLAlchemy ORM*. It features a clean, modular architecture for managing a Product-Category catalog with full CRUD support and pagination.

🌍 *Live Demo:* [https://fastapi-machine-test.onrender.com](https://fastapi-machine-test.onrender.com)  
📄 *API Docs:* [https://fastapi-machine-test.onrender.com/docs](https://fastapi-machine-test.onrender.com/docs)

-----

## 🛠️ Quick Start (Local Setup)

### 1\. Environment & Dependencies

bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Install requirements
pip install -r requirements.txt


### 2\. Database & Config

1.  *MySQL Setup:* Create a database named fastapi-machine.
2.  *Environment File:* Create a .env file in the root:
    env
    DATABASE_URL=mysql+pymysql://root:your_password@localhost:3306/fastapi-machine
    

### 3\. Execution

bash
uvicorn app.main:app --reload


-----

## 📂 API Endpoints

### 🗂️ Categories

  * POST /api/categories — Create new category
  * GET /api/categories?page=1 — List categories (Paginated)
  * GET /api/categories/{id} — Fetch specific category
  * PUT /api/categories/{id} — Update category
  * DELETE /api/categories/{id} — Remove category

### 📦 Products

  * POST /api/products — Create new product
  * GET /api/products?page=1 — List products (includes Category details)
  * GET /api/products/{id} — Fetch specific product
  * PUT /api/products/{id} — Update product
  * DELETE /api/products/{id} — Remove product

-----

## 🏗️ Technical Architecture

### Database Schema

  * *Categories:* id (PK), name (Unique).
  * *Products:* id (PK), name, price, category_id (FK).
  * *Relationship:* *One-to-Many* (One Category contains many Products).

### Key Features

  * *Pagination:* Implemented using limit and offset for optimized data fetching.
  * *Data Validation:* Strict schema enforcement using *Pydantic*.
  * *ORM Logic:* Handles complex relationships; products automatically return nested category objects.
  * *Error Handling:* Custom exception handlers for 404s and validation errors.

-----

## 🧪 Testing Workflow

1.  *Swagger UI:* Navigate to /docs for interactive testing.
2.  *Order of Ops:* 1. Create Category ➡ 2. Create Product (using Category ID) ➡ 3. Test GET/PUT/DELETE.