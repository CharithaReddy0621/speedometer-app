from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)
