import schedule
import time

def scheduled_task():
    print("Running scheduled task...")

def schedule_tasks():
    print("Scheduling tasks...")
    schedule.every(10).minutes.do(scheduled_task)
    while True:
        schedule.run_pending()
        time.sleep(1)
