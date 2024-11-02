from fastapi import FastAPI # type: ignore
from app.routers import image

app = FastAPI(title="Image Generation API")

app.include_router(image.router, prefix="/api/images", tags=["Images"])

@app.get("/")
async def root():
    x=10
    print(x+10)
    return {"message": "Welcome to the Image Generation API","name":"ameya","x":x}
