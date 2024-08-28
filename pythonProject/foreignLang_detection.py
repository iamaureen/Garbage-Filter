
from langdetect import detect, detect_langs, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
import re

# Set seed for reproducibility in detection
DetectorFactory.seed = 0


def detect_foreign_language(text, expected_language='en'):
    """
    Detect if there's any foreign language in the given text.

    Parameters:
    - text (str): The input text to analyze.
    - expected_language (str): The language code for the expected language, default is 'en' for English.

    Returns:
    - foreign_lang_detected (bool): True if a foreign language is detected, False otherwise.
    - languages (list): A list of languages detected in the text.
    """
    # Remove common non-word characters to improve detection
    cleaned_text = re.sub(r'[^\w\s]', '', text)

    try:
        # Detect languages and their probabilities
        lang_probs = detect_langs(cleaned_text)

        # Check if the detected languages include a language other than the expected one
        foreign_lang_detected = any(lang.lang != expected_language for lang in lang_probs)

        return foreign_lang_detected

    except LangDetectException:
        return False


