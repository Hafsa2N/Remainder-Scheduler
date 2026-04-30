#!/usr/bin/env python3
import sys
import argparse
from scheduler import Scheduler

def main():
    parser = argparse.ArgumentParser(description='Reminder Scheduler')
    parser.add_argument('--test', action='store_true', help='Test notification system')
    parser.add_argument('--list', action='store_true', help='List all reminders')
    
    args = parser.parse_args()
    
    if args.test:
        from reminder import Reminder
        test_reminder = Reminder(
            name="Test",
            message="This is a test notification! Your reminder system is working.",
            time_str=None
        )
        test_reminder.send()
        print("Test notification sent!")
        return
    
    if args.list:
        from config import REMINDERS, SCHEDULED_TASKS
        print("\n=== Time-based Reminders ===")
        for r in REMINDERS:
            print(f"  {r['time']} - {r['name']}: {r['message']}")
        print("\n=== Interval-based Tasks ===")
        for t in SCHEDULED_TASKS:
            print(f"  Every {t['interval_minutes']} min - {t['name']}: {t['message']}")
        return
    
    # Run the scheduler
    scheduler = Scheduler()
    scheduler.run()

if __name__ == "__main__":
    main()