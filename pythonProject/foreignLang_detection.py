
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
        print('line 27 :: ', lang_probs)

        # Check if the detected languages include a language other than the expected one
        foreign_lang_detected = any(lang.lang != expected_language for lang in lang_probs)
        print('line 31 :: ', foreign_lang_detected)

        return foreign_lang_detected, lang_probs

    except LangDetectException:
        return False, []


# Example paragraph with mixed languages
paragraph = "This is a test sentence. это компьютерный портал для гиков. This part is in English."

# Detect foreign language
foreign_detected, languages = detect_foreign_language(paragraph)

if foreign_detected:
    print(f"Foreign language detected! Languages found: {languages}")
else:
    print("No foreign language detected.")
