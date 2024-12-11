from monitor import monitor_resources
from optimize import optimize_vdi
from automation import schedule_tasks

if __name__ == "__main__":
    print("Starting VDI Optimizer...")
    monitor_resources()
    optimize_vdi()
    schedule_tasks()