import os, requests
from datetime import date

ROTATION = ["Ariella", "Danielle", "Michael", "Omer", "Or", "Shira", "Yuval"]
ROTATION_START = date(2026, 5, 4)  # Monday of Ariella's first week

def get_oncall():
    weeks_elapsed = (date.today() - ROTATION_START).days // 7
    return ROTATION[weeks_elapsed % len(ROTATION)]

person = get_oncall()
requests.post(os.environ["WEBHOOK_URL"], json={
    "text": f":rotating_light: *On-call this week:* {person}"
})
