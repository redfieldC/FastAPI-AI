from fastapi import APIRouter, HTTPException # type: ignore
from app.models import ImageGenerationRequest, ImageResponse
from app.services import generate_image
from openai import OpenAI
from diffusers import StableDiffusionPipeline


router = APIRouter()

@router.post("/generate", response_model=ImageResponse)
async def generate_image_endpoint(request: ImageGenerationRequest):
    try:
        prompt = request.prompt
        pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
        pipe.to("cuda")  # If you have a GPU

        # Generate an image from text
        image = pipe(prompt).images[0]
        image.show()
        # return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
