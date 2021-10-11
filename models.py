from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

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
    issued_by = Column(String, nullable=True)
    link_id = Column(String, unique=True, index=True)
    order_id = Column(Integer, nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    analysis_date = Column(DateTime, nullable=True)
    result_date = Column(DateTime, nullable=True)
