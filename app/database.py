import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Define SSL arguments for Aiven
# 'ssl_verify_identity': True ensures you are connecting to the actual Aiven server
connect_args = {
    "ssl": {
        "ssl_mode": "REQUIRED"
    }
}

# Create engine with connect_args
engine = create_engine(
    DATABASE_URL, 
    connect_args=connect_args,
    echo=False  # Set to True if you want to see the SQL logs
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

try:
    with engine.connect() as connection:
        # Use .scalar() or .execute()
        result = connection.execute(text("SELECT 1"))
        print("✅ Database connected successfully")
except Exception as e:
    print("❌ Database connection failed:")
    print(f"Error details: {e}")