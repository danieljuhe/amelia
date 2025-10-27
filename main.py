from fastapi import FastAPI

app = FastAPI(title="Amelia API")


@app.get("/ameliastatus")
async def amelia_status():
    return {"status": "running server"}


@app.get("/")
async def root():
    return {"message": "Welcome to Amelia API"}
