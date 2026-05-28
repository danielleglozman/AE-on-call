from http.server import BaseHTTPRequestHandler
from datetime import date
import json

ROTATION = [
    ("Danielle", "U0AA92U6746"),
    ("Michael",  "U087P3ZGTNZ"),
    ("Omer",     "U0AA6FVB3T7"),
    ("Or",       "U0A2L1S6RS5"),
    ("Shira",    "U09Q8LTGB6F"),
    ("Yuval",    "U0AD9805RJT"),
]
ROTATION_START = date(2026, 5, 3)
ROTATION_OFFSET = 3

def get_oncall():
    weeks_elapsed = (date.today() - ROTATION_START).days // 7
    return ROTATION[(ROTATION_OFFSET + weeks_elapsed) % len(ROTATION)]

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        name, user_id = get_oncall()
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({
            "response_type": "in_channel",
            "text": f":rotating_light: *On-call this week:* <@{user_id}|{name.lower()}>"
        }).encode())
