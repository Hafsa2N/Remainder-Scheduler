import time
import logging
from datetime import datetime
from plyer import notification

class Reminder:
    def __init__(self, name, message, time_str=None, interval_minutes=None):
        self.name = name
        self.message = message
        self.time_str = time_str  # For daily reminders (HH:MM format)
        self.interval_minutes = interval_minutes  # For interval-based reminders
        self.last_triggered = None
        
    def should_trigger(self):
        """Check if reminder should be triggered"""
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
        # Daily time-based reminder
        if self.time_str and current_time == self.time_str:
            if not self.last_triggered or self.last_triggered.date() != now.date():
                self.last_triggered = now
                return True
        
        # Interval-based reminder
        if self.interval_minutes:
            if not self.last_triggered:
                self.last_triggered = now
                return True
            else:
                time_diff = (now - self.last_triggered).total_seconds() / 60
                if time_diff >= self.interval_minutes:
                    self.last_triggered = now
                    return True
        
        return False
    
    def send(self):
        """Send desktop notification"""
        try:
            notification.notify(
                title=f"⏰ Reminder: {self.name}",
                message=self.message,
                app_name="Reminder Scheduler",
                timeout=10
            )
            self.log_reminder()
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Reminder sent: {self.name}")
        except Exception as e:
            print(f"Error sending notification: {e}")
            
    def log_reminder(self):
        """Log reminder to file"""
        logging.info(f"Reminder '{self.name}' triggered: {self.message}")