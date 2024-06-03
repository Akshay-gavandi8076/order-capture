from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .schemas import OrderCreate
from .models import Order
from .database import SessionLocal, init_db
from datetime import datetime

app = FastAPI()

# Add CORS middleware to allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Call init_db to initialize database schema when the application starts
init_db()

# Create order
@app.post("/order/", status_code=status.HTTP_201_CREATED)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    try:
        db_order = Order(**order.dict(), captureDate=datetime.now())
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return {"message": "Order created successfully", "order_id": db_order.id}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Failed to create order: {str(e)}")

# Get all orders
@app.get("/orders/")
def get_orders(db: Session = Depends(get_db)):
    try:
        orders = db.query(Order).all()
        return orders
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail=f"Failed to retrieve orders: {str(e)}")
