from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = "postgresql://postgres:password@localhost:5432/todo"

engine = create_engine(db_url)

LocalSession = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

def create_base():
    Base.metadata.create_all(bind = engine)