from fastapi import FastAPI
from core.settings import settings
import uvicorn
from .routes import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.api_host, port=settings.api_port)