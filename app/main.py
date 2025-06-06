from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, posts


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(posts.router)
