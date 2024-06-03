from pydantic import BaseModel
from datetime import date

from app.database import Base

class OrderCreate(BaseModel):
    name: str
    email: str
    phoneNumber: str
    companyName: str
    desiredDeliveryDate: date
    productType: str
    squareMeters: int
    numberOfRolls: int
