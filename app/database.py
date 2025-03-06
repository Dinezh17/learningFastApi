from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



DATABASE_URL = "mssql+pyodbc://@DESKTOP-R1UR1Q4/intern?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"




engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
