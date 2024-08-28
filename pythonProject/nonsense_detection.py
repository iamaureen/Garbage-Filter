import nltk
from nltk.corpus import words
import re

# # Download the words corpus (if not already installed)
# nltk.download('words')

# Load the list of valid English words
valid_words = set(words.words())



def detect_nonsense_words(text):
    """
    Detect and return a list of nonsense words in the text.

    Parameters:
    - text (str): The input text to analyze.

    Returns:
    - nonsense_words (list): A list of detected nonsense words.
    """
    words_in_text = re.findall(r'\b\w+\b', text.lower())  # Extract words and convert to lowercase
    nonsense_words = [word for word in words_in_text if word not in valid_words]
    return nonsense_words


def count_nonsense_words(studentText):
    """
    Count the number of nonsense words in the list.

    Parameters:
    - nonsense_words (list): A list of nonsense words.

    Returns:
    - count (int): The number of nonsense words.
    """
    nonsense_words = detect_nonsense_words(studentText)
    return len(nonsense_words)


def remove_nonsense_words(text):
    """
    Remove all occurrences of nonsense words from the original text.

    Parameters:
    - text (str): The original text.
    - nonsense_words (list): A list of detected nonsense words to be removed.

    Returns:
    - cleaned_text (str): The text with nonsense words removed.
    """
    nonsense_words = detect_nonsense_words(text)
    for word in nonsense_words:
        text = re.sub(r'\b' + re.escape(word) + r'\b', '', text)
    # Clean up extra spaces left after removal
    cleaned_text = re.sub(' +', ' ', text).strip()
    return cleaned_text


