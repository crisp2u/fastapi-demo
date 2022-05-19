
from fastapi import FastAPI, Response
from pydantic import BaseSettings


class Settings(BaseSettings):
    greeting: str = "Hello World!"
    version: str = "n/a"


settings = Settings()
app = FastAPI()


@app.get("/")
def read_root():
    content = f"<p>{settings.greeting}<em>[[{settings.version}]]</em></p>"
    return Response(content=content, media_type="text/html")


@app.get("/health")
def health():
    return "OK"
