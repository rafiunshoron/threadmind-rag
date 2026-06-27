import os
from dotenv import load_dotenv


load_dotenv()


def get_env_var(name: str) -> str:
    """Return an environment variable or raise a clear error."""
    value = os.getenv(name)

    if not value:
        raise ValueError(f"{name} is missing. Please add it to your .env file.")

    return value


GROQ_API_KEY = get_env_var("GROQ_API_KEY")
PINECONE_API_KEY = get_env_var("PINECONE_API_KEY")

PINECONE_INDEX_NAME = get_env_var("PINECONE_INDEX_NAME")
PINECONE_CLOUD = os.getenv("PINECONE_CLOUD", "aws")
PINECONE_REGION = os.getenv("PINECONE_REGION", "us-east-1")

APP_ENV = os.getenv("APP_ENV", "development")