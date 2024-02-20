# from sentence_transformers import SentenceTransformer
import re
from loguru import logger

from openai import OpenAI

client = OpenAI()

# model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")


def clean_readme_text(readme_text):
    logger.debug("Cleaning README text")
    # Cleaning logic as per your requirements
    readme_text = re.sub(r"<.*?>", "", readme_text)  # Remove HTML tags
    # Additional cleaning steps...
    cleaned_text = readme_text.strip()
    logger.debug("README text cleaned")
    return cleaned_text


# def generate_embeddings(readme_text):
#     logger.debug("Generating embeddings for cleaned text")
#     cleaned_text = clean_readme_text(readme_text)
#     embedding = model.encode(cleaned_text, convert_to_tensor=True)
#     embeddings_list = embedding.tolist()
#     logger.debug("Embeddings generated")
#     return embeddings_list


# def generate_embeddings(readme_text, model="text-embedding-3-small"):
#     return client.embeddings.create(input=[readme_text], model=model).data[0].embedding


def generate_embeddings(readme_text, model="text-embedding-3-small"):
    # Split the input text into chunks that do not exceed the model's token limit
    max_length = 8000  # Adjust based on the model's limitations
    chunks = [
        readme_text[i : i + max_length] for i in range(0, len(readme_text), max_length)
    ]

    logger.debug("Generating embeddings for cleaned text")

    all_embeddings = []
    for chunk in chunks:
        # Generate embeddings for each chunk
        chunk_embedding = (
            client.embeddings.create(input=[chunk], model=model).data[0].embedding
        )
        all_embeddings.extend(chunk_embedding)

    logger.debug("Embeddings generated")

    # Optionally, you can average the embeddings from all chunks if needed
    # This step depends on how you plan to use the embeddings
    # Example: averaged_embedding = np.mean(np.array(all_embeddings), axis=0)

    return all_embeddings
