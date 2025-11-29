import requests
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

# In-memory cache
translation_cache = {}

def translate_text(text_list, target_language):
    # Key for caching
    key = "|".join(text_list) + "-" + target_language

    # Switching back to English → return original text
    if target_language == "en":
        return text_list

    # Serve from cache if exists
    if key in translation_cache:
        # print(translation_cache)
        return translation_cache[key]

    translations = []

    for t in text_list:
        # Gemini payload
        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": (
                                f"Translate the following text to {target_language} in the exact wording"
                                "Return ONLY the translated text. No explanation, no alternatives, no formatting. "
                                f"\n\nText: \"{t}\""
                            )
                        }
                    ]
                }
            ]
        }

        response = requests.post(GEMINI_URL, json=payload)

        if response.status_code != 200:
            raise Exception("Gemini API error: " + response.text)

        data = response.json()

        # Correct field extraction
        translated_text = data["candidates"][0]["content"]["parts"][0]["text"]

        translations.append(translated_text)

    # Save in cache
    translation_cache[key] = translations
    return translations



# def translate_text(text_list, target_language):
#     key = '|'.join(text_list) + '-' + target_language

#     if target_language == 'ko' and key in translation_cache:
#         return translation_cache[key]

#     if target_language == 'en':
#         return text_list

#     translations = []
#     for t in text_list:
#         # Replace with actual Gemini API call
#         response = requests.post(GEMINI_URL, json={"text": t, "lang": target_language})
#         translations.append(response.json()['translation'])
#         translations.append(f"KR:{t}")  # placeholder

#     translation_cache[key] = translations
#     return translations
