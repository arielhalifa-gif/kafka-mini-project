from fastapi import FastAPI
import uvicorn
from producer import producer_kafka

app = FastAPI()


@app.post("/register")
def get_json(data: dict):
    producer_kafka(data)
    return {"message": "added a user succesfully"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port="8000")