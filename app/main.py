
from fastapi import FastAPI
from pydantic import BaseSettings


class Settings(BaseSettings):
    greeting: str = "Hello World!"


settings = Settings()
app = FastAPI()


@app.get("/")
def read_root():
    return settings.greeting


@app.get("/health")
def health():
    return "OK"
