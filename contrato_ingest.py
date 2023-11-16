from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd


SQLALCHEMY_DATABASE_URI = 'XXXXXX'

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

Base = declarative_base()

Base.metadata.create_all(bind=engine)

for chunk in pd.read_csv('meutudo_contracts_state.csv', chunksize=100000):
    chunk.to_sql(name='contratos', con=engine, index=False, if_exists='append')