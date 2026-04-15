# 🚀 FastAPI Machine Test

---

## 📌 Project Overview

This project is a REST API built using **FastAPI**, **MySQL**, and **SQLAlchemy ORM**.
It provides complete CRUD operations for **Category** and **Product**, including:

* Pagination using limit & offset
* Relationship handling (Product → Category)
* Clean architecture and modular structure

---

# ⚙️ Installation & Setup

## 1️⃣ Create Virtual Environment

```
python -m venv venv
```

## 2️⃣ Activate Virtual Environment

### Windows

```
venv\Scripts\activate
```

### Mac/Linux

```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Environment Configuration

Create a `.env` file in the root directory:

```
DATABASE_URL=mysql+pymysql://root:your_password@localhost:3306/fastapi-machine
```

---

## 5️⃣ Database Setup

Login to MySQL:

```
mysql -u root -p
```

Create database:

```
CREATE DATABASE fastapi-machine;
```

---

# ▶️ Run the Application

Start the FastAPI server:

```
uvicorn app.main:app --reload
```

---

# 🌐 API Documentation

* Swagger UI:
  http://127.0.0.1:8000/docs

* Postman:
  APIs tested using Postman collection

---

# 🧪 How to Test APIs

1. Start the server
2. Open Swagger UI OR Postman
3. Test APIs in this order:

   * Create Category
   * Create Product
   * Fetch Data
   * Update
   * Delete

---

# 📦 API Endpoints

## 🗂️ Category APIs

| Method | Endpoint                 | Description                 |
| ------ | ------------------------ | --------------------------- |
| POST   | `/api/categories`        | Create category             |
| GET    | `/api/categories?page=1` | Get categories (pagination) |
| GET    | `/api/categories/{id}`   | Get category by ID          |
| PUT    | `/api/categories/{id}`   | Update category             |
| DELETE | `/api/categories/{id}`   | Delete category             |

---

## 📦 Product APIs

| Method | Endpoint               | Description               |
| ------ | ---------------------- | ------------------------- |
| POST   | `/api/products`        | Create product            |
| GET    | `/api/products?page=1` | Get products (pagination) |
| GET    | `/api/products/{id}`   | Get product by ID         |
| PUT    | `/api/products/{id}`   | Update product            |
| DELETE | `/api/products/{id}`   | Delete product            |

---

# 🔗 Relationship Requirement

While fetching a product:

✔ Product details
✔ Associated category details

### Example Response

```json
{
  "id": 8,
  "name": "FormalShoes",
  "price": 1400,
  "category": {
    "id": 16,
    "name": "Footwear"
  }
}
```

---

# 🗄️ Database Design

## Categories Table

* id (Primary Key)
* name (Unique)

## Products Table

* id (Primary Key)
* name
* price
* category_id (Foreign Key)

---

## 🔁 Relationship

* One Category → Many Products
* One Product → One Category

---

# 🧠 Key Concepts Implemented

* SQLAlchemy ORM
* Foreign Key Relationships
* Pagination (offset & limit)
* API validation using Pydantic
* Exception handling

---

# 🧪 Testing

All APIs were tested using **Postman**.

---

# 🏁 Conclusion

This project demonstrates backend development using FastAPI with:

* Clean architecture
* Database integration
* Scalable API design

---
