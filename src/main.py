from fastapi import FastAPI

# core middlewares
from fastapi.middleware.cors import CORSMiddleware

# static files
from fastapi.staticfiles import StaticFiles

# self packages
from core.config import settings
from api.api_v1.router import routers

 
app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(routers)