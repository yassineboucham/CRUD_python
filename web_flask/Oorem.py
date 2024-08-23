from sqlalchemy import DateTime, create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

# Updated connection string with correct password
engine = create_engine('mysql://root:@localhost:3306/crudpy')
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'  # Table name

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    address = Column(String(255), nullable=False, unique=False)
    phone = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, unique=True)

Base.metadata.create_all(engine)

SessionClass = sessionmaker(bind=engine)
session = SessionClass()
