import re
import base64
from loguru import logger
from bs4 import BeautifulSoup


class TextProcessService:
    @staticmethod
    def clean_html_tags(text: str) -> str:
        """
        Remove HTML tags from the given text.

        Args:
            text (str): The text to clean.

        Returns:
            str: The cleaned text.
        """
        logger.info("Starting to clean HTML tags.")
        cleaned_text = re.sub(r"<[^>]+>", "", text)
        logger.info("Finished cleaning HTML tags.")
        return cleaned_text

    @staticmethod
    def decode_base64(text: str) -> str:
        """
        Decode base64 encoded text.

        Args:
            text (str): The base64 encoded text.

        Returns:
            str: The decoded text.
        """
        logger.info("Starting to decode base64 text.")
        try:
            decoded_bytes = base64.b64decode(text)
            decoded_text = decoded_bytes.decode("utf-8")
            logger.info("Successfully decoded base64 text.")
            return decoded_text
        except Exception as e:
            logger.error(f"Failed to decode base64 text: {e}")
            return text

    @staticmethod
    def normalize_text(text: str) -> str:
        """
        Perform basic normalization on the text: lowercasing and removing extra spaces.

        Args:
            text (str): The text to normalize.

        Returns:
            str: The normalized text.
        """
        logger.info("Starting text normalization.")
        text = text.lower()
        text = re.sub(r"\s+", " ", text).strip()
        logger.info("Finished text normalization.")
        return text

    @staticmethod
    def extract_text(html_content: str) -> str:
        """
        Extract textual content from HTML.

        Args:
            html_content (str): The HTML content to extract text from.

        Returns:
            str: The extracted textual content.
        """
        logger.info("Starting to extract text from HTML.")
        soup = BeautifulSoup(html_content, "html.parser")
        text = soup.get_text(separator=" ", strip=True)
        logger.info("Finished extracting text from HTML.")
        return text

    @staticmethod
    def process_text(text: str) -> str:
        """
        Process the README text by cleaning HTML tags, decoding base64 content,
        and normalizing the text.

        Args:
            text (str): The README text to process.

        Returns:
            str: The processed text.
        """
        logger.info("Starting text processing.")
        text = TextProcessService.clean_html_tags(text)
        text = TextProcessService.decode_base64(text)
        text = TextProcessService.normalize_text(text)
        text = TextProcessService.extract_text(text)
        logger.info("Finished text processing.")
        return text
