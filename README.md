# 🧘‍♂️ Fitness Studio Booking API

A simple FastAPI application for managing fitness class bookings. This project demonstrates backend development skills including API design, input validation, timezone handling, in-memory storage, and unit testing.

---

## 🚀 Features

- View all upcoming fitness classes (`/classes`)
- Book a spot in a class (`/book`)
- View all bookings by a client email (`/bookings`)
- Timezone conversion support (default: IST)
- Duplicate booking prevention
- Logging and unit testing
- Swagger UI for easy API interaction

---

## 🛠 Tech Stack

- **Python 3.9+**
- **FastAPI**
- **Pydantic**
- **pytz** (for timezone support)
- **pytest** (for testing)

---

## 📁 Project Structure

├── main.py # FastAPI application and endpoints
├── database.py # In-memory storage and seeding
├── schemas.py # Pydantic models
├── utils.py # Timezone conversion logic
├── test_main.py # Pytest test cases
├── requirements.txt # Python dependencies
└── README.md # Project documentation



---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/fitness-booking-api.git
cd fitness-booking-api


### 2.Install Dependencies
pip install -r requirements.txt



### 3 Run the server
uvicorn main:app --reload


📍 Visit the app: http://127.0.0.1:8000
📘 Swagger UI: http://127.0.0.1:8000/docs

### By Using Swagger UI all postman and curl check can be done

### 4 Running tests
pytest test_main.py




### API Endpoints by using curl


GET /classes
curl -X GET "http://127.0.0.1:8000/classes?timezone=America/New_York"


POST /book
curl -X POST "http://127.0.0.1:8000/book" -H "Content-Type: application/json" \
-d '{"class_id": 1, "client_name": "Shreyas", "client_email": "shreyas@example.com"}'


GET /bookings
curl -X GET "http://127.0.0.1:8000/bookings?client_email=shreyas@example.com"
 	 
