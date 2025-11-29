import requests
import os

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

def update_message(channel_id, ts, blocks):
    headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}
    requests.post(
        "https://slack.com/api/chat.update",
        headers=headers,
        json={"channel": channel_id, "ts": ts, "blocks": blocks}
    )
