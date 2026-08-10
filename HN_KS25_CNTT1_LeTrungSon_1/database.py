from sqlalchemy import create_engine
from sqlalchemy.orm import session_maker, declarative_base

DATABAS_URL = "mysql+pymysql://root:kute9981@localhost:3306/hotel_db"
engine = create_engine()
SessionLocal = session_maker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    
    try:
        yield db
    finally:
        db.close()
        
