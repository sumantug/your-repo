# main.py
from datetime import datetime, timedelta

# Set your execution window start time (UTC)
START_TIME = datetime(2025, 6, 22, 10, 0)  # Change to your desired start UTC time
END_TIME = START_TIME + timedelta(minutes=30)

current_time = datetime.utcnow()

if current_time > END_TIME:
    print(f"⏱️ Skipping: current time {current_time} > end time {END_TIME}")
else:
    print(f"✅ Running task at {current_time}")
    # Your main logic goes here
