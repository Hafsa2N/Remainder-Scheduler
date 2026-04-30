# Reminder configuration
REMINDERS = [
    {
        "name": "Drink Water",
        "message": "Time to stay hydrated! 💧 Drink a glass of water.",
        "time": "10:00"
    },
    {
        "name": "Take a Break",
        "message": "Stand up, stretch, and rest your eyes for 5 minutes.",
        "time": "14:30"
    },
    {
        "name": "Meeting Reminder",
        "message": "Don't forget your daily team meeting!",
        "time": "15:00"
    },
    {
        "name": "End of Day Review",
        "message": "Review what you accomplished today and plan for tomorrow.",
        "time": "17:30"
    }
]

# Scheduled tasks (cron-like format or interval in minutes)
SCHEDULED_TASKS = [
    {"name": "Every Hour Break", "interval_minutes": 60, "message": "Take a 2-minute break! Walk around."},
    {"name": "Daily Backup", "interval_minutes": 1440, "message": "Time to backup your important files."}
]

# Log file location
LOG_FILE = "reminder_log.txt"