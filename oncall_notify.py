import os, requests
from datetime import date

ROTATION = ["Ariella", "Danielle", "Michael", "Omer", "Or", "Shira", "Yuval"]
ROTATION_START = date(2026, 5, 3)  # Sunday when Shira (index 5) started
ROTATION_OFFSET = 5  # Shira's position in the list

def get_oncall():
    weeks_elapsed = (date.today() - ROTATION_START).days // 7
    return ROTATION[(ROTATION_OFFSET + weeks_elapsed) % len(ROTATION)]

person = get_oncall()
requests.post(os.environ["WEBHOOK_URL"], json={
    "text": f":rotating_light: *On-call this week:* {person}"
})
