
from fastapi import FastAPI
from pydantic import BaseSettings


class Settings(BaseSettings):
    greeting: str = "Hello World!"
    version: str = "n/a"


settings = Settings()
app = FastAPI()


@app.get("/")
def read_root():
    return f"<p>{settings.greeting}</p><div><em>{settings.version}</em></div>."


@app.get("/health")
def health():
    return "OK"
