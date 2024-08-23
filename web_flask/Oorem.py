from sqlalchemy import DateTime, create_engine, Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Updated connection string with correct password
#'mysql+pymysql://username:password@localhost/mydatabase'
engine = create_engine('mysql://root:@localhost:3306/crudpy')
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'  # Table name
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    address = Column(String(255))
    phone = Column(String(255))
    password = Column(String(255))
    created_at = Column(DateTime)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
