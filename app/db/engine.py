from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:mysecretpassword@localhost:5432/app_text_analyzer_db"

engine = create_engine(DATABASE_URL, echo=True)