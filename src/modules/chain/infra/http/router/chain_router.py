from __future__ import annotations

from fastapi import APIRouter

from src.modules.chain.useCases.chat.chain_chat_usecase import chain_chat_usecase

chain_router = APIRouter(tags=["Chain"], prefix="/chain")

chain_router.post("/chat")(chain_chat_usecase)
