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


class RequestResponse(RequestItem):
    id: int
    link_id: str
    order_id: int = None

    class Config:
        orm_mode = True
