from fastapi import FastAPI, HTTPException, Query
from typing import List
from schemas import FitnessClass, BookingRequest, Booking
from database import fitness_classes, bookings, seed_data
from utils import convert_timezone

import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Fitness Studio Booking API")

# Seed initial classes
seed_data()
print("Classes seeded in main.py:", fitness_classes)



@app.get("/")
def root():
    return {
        "message": "Welcome to the Fitness Studio Booking API!",
        "swagger_ui": "Access the interactive Swagger UI here: http://127.0.0.1:8000/docs"
    }

@app.get("/classes", response_model=List[FitnessClass])
def get_classes(timezone: str = Query("Asia/Kolkata", description="Target timezone e.g. America/New_York")):
    """
    Return all upcoming classes in the requested timezone.
    """
    try:
        class_list = []
        for cls in fitness_classes.values():
            updated_time = convert_timezone(cls.datetime, timezone)
            updated_class = cls.copy(update={"datetime": updated_time})
            class_list.append(updated_class)
        return class_list
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/book", response_model=Booking)
def book_class(request: BookingRequest):
    """
    Book a class by ID if slots are available.
    Prevent duplicate bookings by the same client for the same class.
    """
    fitness_class = fitness_classes.get(request.class_id)
    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")

    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")
    
    # Prevent duplicate bookings by the same client for this class
    for b in bookings:
        if b.class_id == request.class_id and b.client_email == request.client_email:
            raise HTTPException(status_code=400, detail="You have already booked this class")

    # Reduce the number of available slots
    fitness_class.available_slots -= 1

    booking = Booking(
        class_id=fitness_class.id,
        class_name=fitness_class.name,
        client_name=request.client_name,
        client_email=request.client_email,
        datetime=fitness_class.datetime,
        instructor=fitness_class.instructor
    )

    bookings.append(booking)
    logger.info(f"Booked: {booking}")
    return booking


@app.get("/bookings", response_model=List[Booking])
def get_bookings(client_email: str = Query(..., description="Client email to fetch bookings")):
    """
    Return all bookings made by a specific email address.
    """
    results = [b for b in bookings if b.client_email == client_email]
    if not results:
        raise HTTPException(status_code=404, detail="No bookings found for this email")
    return results
