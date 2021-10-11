from typing import Optional
from pydantic import BaseModel, EmailStr


class RequestItem(BaseModel):
    name: str
    last_name: str
    patronymic: str
    phone: str
    email: EmailStr
    birthdate: str
    serial_number: str
    issued_by: str
    address: Optional[str] = None
    analysis_date: Optional[str] = None
