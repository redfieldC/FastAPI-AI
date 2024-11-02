import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    REPLICATE_API_TOKEN: str = os.getenv("REPLICATE_API_TOKEN")

settings = Settings()
