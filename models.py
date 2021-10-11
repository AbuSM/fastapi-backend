from sqlalchemy import Column, Integer, String, DateTime

from database import Base


class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=False, index=True)
    name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    address = Column(String)
    phone = Column(String)
    birthdate = Column(String)
    serial_number = Column(String)
    issued_by = Column(String)
    link_id = Column(String, unique=True, index=True)
    order_id = Column(Integer, unique=True, index=True)
    created_date = Column(DateTime)
    analysis_date = Column(DateTime)
    result_date = Column(DateTime)