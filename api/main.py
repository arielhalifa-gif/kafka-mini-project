from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.post("/register")