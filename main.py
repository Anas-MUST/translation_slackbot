from fastapi import FastAPI
from translate import router as translate_router

app = FastAPI()
app.include_router(translate_router)



























# # from fastapi import FastAPI
# # from translate import router as translate_router

# # app = FastAPI()
# # app.include_router(translate_router)


# # # main.py
# from fastapi import FastAPI, Request
# import os
# import requests
# # from dotenv import load_dotenv
# from gemini_service import translate_text

# # load_dotenv()

# # SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# app = FastAPI()
# from translate import router as translate_router
# app.include_router(translate_router)
# # --- Translation API endpoint ---
# @app.post("/translate")
# async def translate_endpoint(req: Request):
#     data = await req.form()
#     text_list = data.get("text", [])
#     target_language = data.get("target_language", "en")
#     translated = translate_text(text_list, target_language)
#     return {"translations": translated}


# from fastapi import APIRouter, Request, HTTPException
# from typing import List
# # We'll use this to run the synchronous translate_text function in a background thread
# import anyio 


# @app.post("/translate")
# async def translate_endpoint(req: Request):
#     # Data parsing is correct for a standard JSON body
#     try:
#         data = await req.json()
#     except Exception:
#         # Handle cases where the body is not valid JSON
#         raise HTTPException(status_code=400, detail="Request body must be valid JSON.")

#     # 1. Extract inputs with default values
#     text_list: List[str] = data.get("text", [])
#     target_language: str = data.get("target_language", "en")
    
#     # 2. Add validation for text_list
#     if not isinstance(text_list, list):
#          raise HTTPException(status_code=422, detail="Field 'text' must be a list of strings.")

#     # 3. CRITICAL CHANGE: Run the synchronous function in a threadpool
#     try:
#         translated = await anyio.to_thread.run_sync(
#             translate_text, text_list, target_language
#         )
#     except Exception as e:
#         # Catch any errors that occur during the translation (e.g., Gemini API error, network error)
#         print(f"Translation Error: {e}")
#         raise HTTPException(status_code=500, detail="Translation service failed.")
        
#     return {"translations": translated}

# Note: You need to install anyio if you haven't already: pip install anyio


# # --- Slack action endpoint (button / toggle) ---
# @app.post("/slack/action")
# async def slack_action(req: Request):
#     payload = await req.json()

#     # Example for button action
#     if "actions" in payload:
#         action_id = payload['actions'][0]['action_id']

#         # Extract message blocks
#         blocks = payload['message']['blocks']
#         channel_id = payload['channel']['id']
#         message_ts = payload['message']['ts']

#         # Extract text from section blocks
#         text_to_translate = []
#         mapping = []
#         for i, block in enumerate(blocks):
#             if block['type'] == 'section' and 'text' in block:
#                 text_to_translate.append(block['text']['text'])
#                 mapping.append(i)

#         # Decide target language
#         if action_id == "translate_button":
#             target_language = "ko"
#         else:
#             target_language = "en"

#         # Call translation
#         translated_texts = translate_text(text_to_translate, target_language)

#         # Replace text in blocks
#         for idx, i in enumerate(mapping):
#             blocks[i]['text']['text'] = translated_texts[idx]

#         # Update Slack message
#         headers = {"Authorization": f"Bearer {SLACK_BOT_TOKEN}"}
#         requests.post(
#             "https://slack.com/api/chat.update",
#             headers=headers,
#             json={
#                 "channel": channel_id,
#                 "ts": message_ts,
#                 "blocks": blocks
#             }
#         )

#     # Return success
#     return {"ok": True}
