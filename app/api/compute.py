from fastapi import APIRouter, Body, Response
from app.schemas import Compute_input
from starlette.responses import JSONResponse
import logging, os, json

router = APIRouter()

@router.post("/compute", status_code=200)
def compute(req: Compute_input = Body(...)) -> JSONResponse:
    try:
        if req:
            y = (req.m * req.x) + req.c
            return JSONResponse(
                status_code=200,
                content={
                    "y": y
                }
            )
        else:
            return JSONResponse(
                status_code = 400,
                content = {
                    "message": "Invalid Request"
                }
            )
    except Exception as e:
        logging.error(e)
        return JSONResponse(
            status_code=400,
            content={
                "message": "error"
            }
        )