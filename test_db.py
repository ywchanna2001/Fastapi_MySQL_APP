# test_db.py
from database import engine

try:
    with engine.connect() as conn:
        print("✅ Successfully connected to the database!")
except Exception as e:
    print("❌ Failed to connect to the database:", e)
