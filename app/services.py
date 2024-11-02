import replicate
import os
import requests

from app.config import settings
from app.models import ImageResponse
from diffusers import DiffusionPipeline
import torch
replicate_api_token = os.getenv("REPLICATE_API_TOKEN")
from openai import OpenAI

def generate_image(prompt: str) -> ImageResponse:
    client = OpenAI()

    response = client.images.generate(
      model="dall-e-3",
      prompt=prompt,
      size="1024x1024",
      quality="standard",
      n=1,
    )

    image_url = response.data[0].url

