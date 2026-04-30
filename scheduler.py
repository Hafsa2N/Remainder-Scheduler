import time
import logging
from datetime import datetime
from reminder import Reminder
from config import REMINDERS, SCHEDULED_TASKS, LOG_FILE

class Scheduler:
    def __init__(self):
        self.reminders = []
        self.setup_logging()
        self.load_reminders()
        
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            filename=LOG_FILE,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
    def load_reminders(self):
        """Load reminders from config"""
        # Load time-based reminders
        for reminder_config in REMINDERS:
            reminder = Reminder(
                name=reminder_config["name"],
                message=reminder_config["message"],
                time_str=reminder_config["time"]
            )
            self.reminders.append(reminder)
        
        # Load interval-based tasks
        for task_config in SCHEDULED_TASKS:
            reminder = Reminder(
                name=task_config["name"],
                message=task_config["message"],
                interval_minutes=task_config["interval_minutes"]
            )
            self.reminders.append(reminder)
            
        print(f"Loaded {len(self.reminders)} reminders")
        
    def run(self):
        """Main scheduler loop"""
        print(f"Reminder Scheduler started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("Press Ctrl+C to stop\n")
        
        try:
            while True:
                for reminder in self.reminders:
                    if reminder.should_trigger():
                        reminder.send()
                time.sleep(30)  # Check every 30 seconds
        except KeyboardInterrupt:
            print("\nScheduler stopped")
            logging.info("Scheduler stopped by user")