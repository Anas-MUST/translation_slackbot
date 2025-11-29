from fastapi import APIRouter
from pydantic import BaseModel
from gemini_service import translate_text

router = APIRouter()

class TranslateRequest(BaseModel):
    text: list[str]
    target_language: str

# @router.post("/translate")
# def translate(req: TranslateRequest):
#     try:
#         translations = translate_text(req.text, req.target_language)
#         return {"translations": translations}
#     except Exception:
#         return {"error": "Translation failed"}


import traceback

@router.post("/translate")
def translate(req: TranslateRequest):
    print(traceback.format_exc())
    try:
        translations = translate_text(req.text, req.target_language)
        return {"translations": translations}
    except Exception:
        print(traceback.format_exc())
        print("-------------------------------")
        return {"error": "Translation failed"}











# from fastapi import APIRouter
# from pydantic import BaseModel
# from gemini_service import translate_text

# import traceback


# router = APIRouter()

# class TranslateRequest(BaseModel):
#     text: list[str]
#     target_language: str

# @router.post("/translate")
# def translate(req: TranslateRequest):
#     print(traceback.format_exc())
#     try:
#         translations = translate_text(req.text, req.target_language)
#         return {"translations": translations}
#     except Exception:
#         print(traceback.format_exc())
#         print("-------------------------------")
#         return {"error": "Translation failed"}

# # @router.get("/translate")
# # def simple():
# #     return {"translations"}
    