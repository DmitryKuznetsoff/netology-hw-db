from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB:
    db = f'postgresql://netology:123456@localhost:5432/netology_orm_hw'
    engine = create_engine(db)
    session = sessionmaker(bind=engine)()
