from datetime import datetime, timedelta, timezone

# Set your new execution window
START_TIME = datetime(2025, 6, 22, 5, 45, tzinfo=timezone.utc)
END_TIME = START_TIME + timedelta(minutes=30)

current_time = datetime.now(timezone.utc)

if current_time > END_TIME:
    print(f"⏱️ Skipping: current time {current_time} > end time {END_TIME}")
else:
    print(f"✅ Running task at {current_time}")
    # Your logic here

with open("execution_log.txt", "a") as f:
    f.write(f"{current_time} - Ran: {current_time <= END_TIME}\n")
