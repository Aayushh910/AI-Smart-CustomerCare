from fastapi import APIRouter
from app.schemas.message_schema import MessageCreate, MessageResponse
from app.services.chat_service import get_chatbot_response

router = APIRouter()

@router.post("/chat", response_model=MessageResponse)
def chat(request: MessageCreate):

    reply = get_chatbot_response(request.message)

    return {"reply": reply}