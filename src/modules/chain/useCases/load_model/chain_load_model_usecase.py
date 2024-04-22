from __future__ import annotations

from fastapi import Body
from starlette.responses import JSONResponse

from src.core.responses import json_response
from src.modules.chain.useCases.load_model.chain_load_model_dto import ChainLoadModelDTO


async def user_create_usecase(model: ChainLoadModelDTO = Body(..., embed=False)) -> JSONResponse:
    return json_response(status_code=200, content={
        "message": "Model is now loading",
    })
