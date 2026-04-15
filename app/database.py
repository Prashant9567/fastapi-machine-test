import os
from platform import machine
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker,declarative_base

load_dotenv()  # Load environment from .env file

DATABASE_URL=os.getenv("DATABASE_URL")  #Get Database URL from .env
print(f"Using Database URL: {DATABASE_URL}")  

engine=create_engine(DATABASE_URL)  #Create Database Engine

SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)  #Create Session Local

# Base class for models
Base = declarative_base()

try:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
        print("✅ Database connected successfully")
except Exception as e:
    print("❌ Database connection failed:", e)
