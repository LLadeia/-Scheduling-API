from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "ok"}

from fastapi import FastAPI
from app.api import auth

app = FastAPI()

app.include_router(auth.router)


from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)