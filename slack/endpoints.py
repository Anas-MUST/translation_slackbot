from fastapi import APIRouter, Request
import os
import requests
from gemini_service import translate_text

router = APIRouter()
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

@router.post("/action")
async def slack_action(req: Request):
    payload = await req.json()

    if "actions" in payload:
        action_id = payload['actions'][0]['action_id']
        blocks = payload['message']['blocks']
        channel_id = payload['channel']['id']
        message_ts = payload['message']['ts']

        # Extract texts from blocks
        text_to_translate = []
        mapping = []
        for i, block in enumerate(blocks):
            if block['type'] == 'section' and 'text' in block:
                text_to_translate.append(block['text']['text'])
                mapping.append(i)

        target_language = "ko" if action_id == "translate_button" else "en"
        translated_texts = translate_text(text_to_translate, target_language)

        # Replace text in blocks
        for idx, i in enumerate(mapping):
            blocks[i]['text']['text'] = translated_texts[idx]

        # Update Slack message
        headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}
        requests.post(
            "https://slack.com/api/chat.update",
            headers=headers,
            json={"channel": channel_id, "ts": message_ts, "blocks": blocks}
        )

    return {"ok": True}
