# from sentence_transformers import SentenceTransformer
import re
from loguru import logger

# model = SentenceTransformer("all-MiniLM-L6-v2", device="cpu")


def clean_readme_text(readme_text):
    logger.debug("Cleaning README text")
    # Cleaning logic as per your requirements
    readme_text = re.sub(r"<.*?>", "", readme_text)  # Remove HTML tags
    # Additional cleaning steps...
    cleaned_text = readme_text.strip()
    logger.debug("README text cleaned")
    return cleaned_text


def generate_embeddings(readme_text):
    logger.debug("Generating embeddings for cleaned text")
    cleaned_text = clean_readme_text(readme_text)
    embedding = model.encode(cleaned_text, convert_to_tensor=True)
    embeddings_list = embedding.tolist()
    logger.debug("Embeddings generated")
    return embeddings_list
