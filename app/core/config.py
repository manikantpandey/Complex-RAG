from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    embedding_model: str = "text-embedding-3-small"
    groq_api_key: str
    groq_model_name: str = "groq-llama-3-70b-instruct"

    class Config:
        env_file = ".env"
        
settings = Settings()