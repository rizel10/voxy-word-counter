from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from typing import Annotated


class TextContent(BaseModel):
  content: Annotated[str, Form()]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.post("/")
def word_count(content: Annotated[str, Form()]):
    return len(content.strip().split())
