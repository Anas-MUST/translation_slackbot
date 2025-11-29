# from fastapi import FastAPI, Request
# import requests
# import os
# from gemini_service import translate_text

# SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
# app = FastAPI()

# @app.post("/slack/workflow-action")
# async def workflow_action(req: Request):
#     payload = await req.json()
    
#     # Extract toggle value
#     language = payload['inputs']['language_toggle']['value']
    
#     # Extract blocks or form data
#     blocks = payload['blocks']  # or modal view blocks
    
#     # Collect texts
#     texts = []
#     mapping = []
#     for i, block in enumerate(blocks):
#         if block['type'] == 'section' and 'text' in block:
#             texts.append(block['text']['text'])
#             mapping.append(i)
#         elif block['type'] == 'input':
#             texts.append(block['label']['text'])
#             mapping.append(i)
    
#     # Call translation API if Korean
#     if language == 'ko':
#         translations = translate_text(texts, 'ko')
#     else:
#         translations = texts  # English → restore original
    
#     # Replace text in blocks
#     for idx, i in enumerate(mapping):
#         if blocks[i]['type'] == 'section':
#             blocks[i]['text']['text'] = translations[idx]
#         elif blocks[i]['type'] == 'input':
#             blocks[i]['label']['text'] = translations[idx]
    
#     # Update Slack message or modal
#     if payload.get('view_id'):
#         # Modal
#         requests.post(
#             "https://slack.com/api/views.update",
#             headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN}"},
#             json={"view_id": payload['view_id'], "view": {"blocks": blocks}}
#         )
#     else:
#         # Message
#         requests.post(
#             "https://slack.com/api/chat.update",
#             headers={"Authorization": f"Bearer {SLACK_BOT_TOKEN}"},
#             json={"channel": payload['channel']['id'], "ts": payload['message']['ts'], "blocks": blocks}
#         )

#     return {"status": "ok"}
