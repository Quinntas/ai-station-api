from __future__ import annotations

from fastapi import Body
from starlette.responses import JSONResponse

from src.core.responses import json_response
from src.modules.chain.infra.lang_chain.agents import agent_executor
from src.modules.chain.useCases.chat.chain_chat_dto import ChainChatDTO
from src.utils.env import env


async def chain_chat_usecase(dto: ChainChatDTO = Body(..., embed=False)) -> JSONResponse:
    res = agent_executor.invoke({
        env.CHAIN_INPUT_KEY: dto.input,
        env.CHAIN_MEMORY_KEY: [history.__dict__ for history in dto.history],
        env.CHAIN_SYSTEM_INPUT: dto.system,
    })

    return json_response(status_code=200, content={
        "message": res["output"],
    })
