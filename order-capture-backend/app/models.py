from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phoneNumber = Column(String, index=True)
    companyName = Column(String, index=True)
    desiredDeliveryDate = Column(Date, index=True)
    productType = Column(String, index=True)
    numberOfRolls = Column(Integer)
    squareMeters = Column(Integer)
    captureDate = Column(Date, index=True)
