
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
        lang_probs = detect_langs(text)

        # Check if the detected languages include a language other than the expected one
        foreign_lang_detected = any(lang.lang != expected_language for lang in lang_probs)

        print("line 32 :: ", foreign_lang_detected)

        return foreign_lang_detected

    except LangDetectException:
        return False


def proportion_foreign(text, target_language='en'):
    sentences = text.split('.')
    total_sentences = len(sentences)
    foreign_sentences = 0

    for sentence in sentences:
        try:
            if sentence.strip():  # Check if the sentence is not empty
                if detect(sentence.strip()) != target_language:
                    foreign_sentences += 1
        except LangDetectException:
            foreign_sentences += 1

    percentage_foreign = (foreign_sentences / total_sentences) * 100 if total_sentences > 0 else 0
    return percentage_foreign

def remove_foreign_language(text, target_language='en'):
    sentences = text.split('.')
    filtered_sentences = []

    for sentence in sentences:
        try:
            if detect(sentence.strip()) == target_language:
                filtered_sentences.append(sentence.strip())
        except LangDetectException:
            continue

    return '. '.join(filtered_sentences) + '.'

if __name__ == "__main__":
    texts = "This is an English sentence damn. Esta es una frase en español. Another English sentence"

    print(detect_foreign_language(texts))
    print(remove_foreign_language(texts))