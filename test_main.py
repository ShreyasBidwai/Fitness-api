# test_main.py

import pytest
from fastapi.testclient import TestClient
from main import app
from database import seed_data, fitness_classes

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_data():
    # This ensures fresh data for each test
    seed_data()

def test_get_classes():
    response = client.get("/classes")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_successful_booking():
    booking_data = {
        "class_id": 1,
        "client_name": "Test User",
        "client_email": "test@example.com"
    }
    response = client.post("/book", json=booking_data)
    assert response.status_code == 200
    data = response.json()
    assert data["client_email"] == "test@example.com"
    assert data["class_id"] == 1

def test_duplicate_booking_prevention():
    booking_data = {
        "class_id": 1,
        "client_name": "Test User",
        "client_email": "test@example.com"
    }
    client.post("/book", json=booking_data)
    duplicate_response = client.post("/book", json=booking_data)
    assert duplicate_response.status_code == 400
    assert duplicate_response.json()["detail"] == "You have already booked this class"

def test_slot_decreases_after_booking():
    class_id = 1
    original_slots = fitness_classes[class_id].available_slots

    booking_data = {
        "class_id": class_id,
        "client_name": "Test User",
        "client_email": "slotcheck@example.com"
    }
    client.post("/book", json=booking_data)

    updated_slots = fitness_classes[class_id].available_slots
    assert updated_slots == original_slots - 1
