from fastapi import FastAPI

from app.endpoints import router as endpoints_router

app = FastAPI()

app.include_router(endpoints_router)
