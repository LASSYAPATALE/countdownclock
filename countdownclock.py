import datetime
import time

def countdown_timer(end_date):
    while end_date > datetime.datetime.now():
        time_remaining = end_date - datetime.datetime.now()
        print(f"Time remaining: {time_remaining}", end="\r")
        time.sleep(1)

    print("\nCountdown complete!")

# Example: Set the end date and time
end_date = datetime.datetime(2024, 2, 28, 12, 0, 0)  # Replace with your specific date and time

countdown_timer(end_date)