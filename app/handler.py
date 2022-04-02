from fastapi import FastAPI
from .api import compute

app = FastAPI()

app.include_router(
    compute.router,
    responses={404: {"message": "Not Found"}},
)