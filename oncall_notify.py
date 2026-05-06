import os, requests
from datetime import date

ROTATION = [
    ("Ariella", "U07U79M62K1"),
    ("Danielle", "U0AA92U6746"),
    ("Michael", "U087P3ZGTNZ"),
    ("Omer",    "U0AA6FVB3T7"),
    ("Or",      "U0A2L1S6RS5"),
    ("Shira",   "U09Q8LTGB6F"),
    ("Yuval",   "U0AD9805RJT"),
]
ROTATION_START = date(2026, 5, 3)
ROTATION_OFFSET = 5

def get_oncall(week_offset=0):
    weeks_elapsed = (date.today() - ROTATION_START).days // 7 + week_offset
    return ROTATION[(ROTATION_OFFSET + weeks_elapsed) % len(ROTATION)]

week_offset = int(os.environ.get("WEEK_OFFSET", "0"))
name, user_id = get_oncall(week_offset)
message = (
    f":calendar: *Heads up! On-call next week:* <@{user_id}|{name.lower()}>"
    if week_offset == 1
    else f":rotating_light: *On-call this week:* <@{user_id}|{name.lower()}>"
)

requests.post(os.environ["WEBHOOK_URL"], json={
    "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": message}}]
})
