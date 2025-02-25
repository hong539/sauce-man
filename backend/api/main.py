from fastapi import FastAPI
from api.routes import router
from api.database import engine
from api.models import Base

app = FastAPI()

# 建立資料表
Base.metadata.create_all(bind=engine)

# 註冊路由
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)