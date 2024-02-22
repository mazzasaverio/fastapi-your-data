from abc import ABC, abstractmethod
from typing import List
import numpy as np
from loguru import logger

# Import OpenAI GPT-3
from openai import OpenAI

from app.core.config import settings

# # Import Sentence Transformers
# from sentence_transformers import SentenceTransformer


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
        chunks = [
            readme_text[i : i + max_length]
            for i in range(0, len(readme_text), max_length)
        ]

        logger.debug("Generating embeddings for cleaned text")

        all_embeddings = []
        for chunk in chunks:
            # Generate embeddings for each chunk
            chunk_embedding = (
                self.client.embeddings.create(input=[chunk], model=model)
                .data[0]
                .embedding
            )
            all_embeddings.extend(chunk_embedding)

        logger.debug("Embeddings generated")

        # Optionally, you can average the embeddings from all chunks if needed
        # This step depends on how you plan to use the embeddings
        # Example: averaged_embedding = np.mean(np.array(all_embeddings), axis=0)

        return all_embeddings

    # async def generate_embeddings(self, readme_text, model="text-embedding-3-small"):
    #     logger.info("Starting to generate embeddings")
    #     max_length = 8000  # Adjust based on the model's limitations
    #     chunks = [
    #         readme_text[i : i + max_length]
    #         for i in range(0, len(readme_text), max_length)
    #     ]

    #     logger.debug("Generating embeddings for cleaned text")

    #     all_embeddings = []
    #     for chunk in chunks:
    #         logger.debug(f"Generating embeddings for chunk with length {len(chunk)}")
    #         chunk_embedding = (
    #             await self.client.embeddings.create(input=[chunk], model=model)
    #             .data[0]
    #             .embedding
    #         )
    #         all_embeddings.extend(chunk_embedding)

    #     logger.debug("Embeddings generated")

    #     return all_embeddings


# class SentenceTransformerEmbeddingService(EmbeddingGenerator):
#     def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
#         logger.info(f"Initializing SentenceTransformerEmbeddingService with model: {model_name}")
#         self.model = SentenceTransformer(model_name)

#     def generate_embeddings(self, text: str) -> List[float]:
#         logger.info("Starting to generate embeddings using SentenceTransformer")
#         embedding = self.model.encode(text)
#         logger.debug("Embeddings generated")
#         return embedding.tolist()


class EmbeddingService:
    def __init__(self, strategy: str = "openai", api_key: str = None):
        logger.info(f"Initializing EmbeddingService with strategy: {strategy}")
        if strategy == "openai" and api_key:
            self.strategy = OpenAIEmbeddingService(api_key=api_key)
        # elif strategy == "sentence_transformer":
        #     self.strategy = SentenceTransformerEmbeddingService()
        else:
            logger.error("Invalid embedding strategy or missing API key for OpenAI.")
            raise ValueError(
                "Invalid embedding strategy or missing API key for OpenAI."
            )

    def generate_embeddings(self, text: str) -> List[float]:
        logger.info("Generating embeddings for given text")

        embeddings = self.strategy.generate_embeddings(text)

        logger.debug(f"Embeddings generated: {embeddings}")

        return embeddings
