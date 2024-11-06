from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine('sqlite:///taskmanager.db', echo=True)

SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
    # def __init__(self):
    #     super().__init__()


# class User(Base):
#     pass
