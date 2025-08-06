from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def test():
    return {"message": "Welcome to my GitHub book manager projects!"}