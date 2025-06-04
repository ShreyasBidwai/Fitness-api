from typing import List, Dict
from schemas import FitnessClass, Booking
from datetime import datetime
import pytz

# Simulated in-memory data store
fitness_classes: Dict[int, FitnessClass] = {}
bookings: List[Booking] = []

# IST Timezone
IST = pytz.timezone("Asia/Kolkata")

# Seed sample fitness classes (in IST)
def seed_data():
    fitness_classes.clear()  # Clear any existing data

    fitness_classes.update({
        1: FitnessClass(
            id=1,
            name="Yoga",
            datetime=IST.localize(datetime(2025, 6, 5, 7, 0)),
            instructor="Swami Ramdev",
            available_slots=5
        ),
        2: FitnessClass(
            id=2,
            name="Zumba",
            datetime=IST.localize(datetime(2025, 6, 5, 9, 0)),
            instructor="Shweta",
            available_slots=8
        ),
        3: FitnessClass(
            id=3,
            name="HIIT",
            datetime=IST.localize(datetime(2025, 6, 5, 18, 0)),
            instructor="Gautam",
            available_slots=6
        )
    })

