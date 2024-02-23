from abc import ABC, abstractmethod
from typing import List
import numpy as np
from loguru import logger
from openai import OpenAI
from app.core.config import settings


class EmbeddingGenerator(ABC):
    @abstractmethod
    async def generate_embeddings(self, text: str) -> List[float]:
        pass


class OpenAIEmbeddingService(EmbeddingGenerator):
    def __init__(self, model: str = "text-embedding-ada-002", api_key: str = None):
        logger.info(f"Initializing OpenAIEmbeddingService with model: {model}")
        self.api_key = api_key

        self.model = model
        self.client = OpenAI(api_key=api_key)

    def generate_embeddings(self, readme_text, model="text-embedding-3-small"):
        # Split the input text into chunks that do not exceed the model's token limit
        max_length = 8000  # Adjust based on the model's limitations
        text = readme_text[:max_length]

        embedding = (
            self.client.embeddings.create(input=[text], model=model).data[0].embedding
        )

        return embedding


class EmbeddingService:
    def __init__(self, strategy: str = "openai", api_key: str = None):
        logger.info(f"Initializing EmbeddingService with strategy: {strategy}")
        if strategy == "openai" and api_key:
            self.strategy = OpenAIEmbeddingService(api_key=api_key)
        else:
            logger.error("Invalid embedding strategy or missing API key for OpenAI.")
            raise ValueError(
                "Invalid embedding strategy or missing API key for OpenAI."
            )

    def generate_embeddings(self, text: str) -> List[float]:

        embeddings = self.strategy.generate_embeddings(text)

        return embeddings
