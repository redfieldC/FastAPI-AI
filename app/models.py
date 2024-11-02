from pydantic import BaseModel

class ImageGenerationRequest(BaseModel):
    prompt: str
    size: str = "1365x1024"  # Default size for the generated image

class ImageResponse(BaseModel):
    image_url: str
