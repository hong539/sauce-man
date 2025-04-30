from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
import datetime
from api.database import get_db
from api.models import Message

router = APIRouter()


class MessageData(BaseModel):
    content: str
    author: str
    timestamp: str


class MessageDumpRequest(BaseModel):
    channel: str
    member: str
    before_date: Optional[str] = None
    after_date: Optional[str] = None
    messages: List[MessageData]


@router.post("/save_messages")
async def save_messages(request: MessageDumpRequest, db: Session = Depends(get_db)):
    """處理 Discord Bot 傳來的訊息並存入資料庫"""
    try:
        messages = [
            Message(
                channel=request.channel,
                member=request.member,
                content=msg.content,
                timestamp=datetime.datetime.fromisoformat(msg.timestamp),
            )
            for msg in request.messages
        ]
        db.add_all(messages)
        db.commit()
        return {"status": "success", "message_count": len(messages)}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"資料庫錯誤: {str(e)}")
