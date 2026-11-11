
from pydantic import BaseModel, ConfigDict, EmailStr


class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str


class CustomerUpdate(CustomerCreate):
    pass


class CustomerResponse(CustomerCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
