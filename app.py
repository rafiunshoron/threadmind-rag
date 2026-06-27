from utils.config import (
    GROQ_API_KEY,
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
    PINECONE_CLOUD,
    PINECONE_REGION,
    APP_ENV,
)


def main() -> None:
    print("ThreadMind RAG setup check")
    print("--------------------------")
    print("GROQ_API_KEY found:", bool(GROQ_API_KEY))
    print("PINECONE_API_KEY found:", bool(PINECONE_API_KEY))
    print("PINECONE_INDEX_NAME:", PINECONE_INDEX_NAME)
    print("PINECONE_CLOUD:", PINECONE_CLOUD)
    print("PINECONE_REGION:", PINECONE_REGION)
    print("APP_ENV:", APP_ENV)


if __name__ == "__main__":
    main()