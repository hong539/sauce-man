from fastapi import FastAPI
from .routes import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    from .config import API_HOST, API_PORT
    uvicorn.run(app, host=API_HOST, port=API_PORT)