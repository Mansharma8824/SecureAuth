from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# 1. Database location
DATABASE_URL = "sqlite:///./secureauth.db"

# 2.  Create the database engine

engine = create_engine(
    DATABASE_URL,
    connect_args= {"check_same_thread":False}
)

# 3. create a fectory for database sessions

SessionLocal = sessionmaker(
    bind= engine,
    autoflush= False,
    autocommit = False
)

# 4. Base class for database models

class Base(DeclarativeBase):
    pass

# 4. provide database session to API endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
        
