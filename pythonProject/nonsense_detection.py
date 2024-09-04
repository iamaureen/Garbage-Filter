import re
from nostril import nonsense
from spellchecker import SpellChecker

# Initialize the spell checker
spell = SpellChecker()

def detect_nonsense_words(text):
    """
    Detect and return a list of nonsense words in the text.

    Parameters:
    - text (str): The input text to analyze.

    Returns:
    - nonsense_words (list): A list of detected nonsense words.
    """

    words = text.split()
    nonsense_words = []

    for word in words:
        if len(word) >= 6:
            if nonsense(word):
                nonsense_words.append(word)
        else:
            # Check shorter words for spelling errors
            if word not in spell:
                nonsense_words.append(word)

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
    print(nonsense_words)
    for word in nonsense_words:
        text = text.replace(word, "")
    # Clean up extra spaces left after removal
    text = re.sub(' +', ' ', text).strip()
    return text


if __name__ == "__main__":
    studentText = ("This is a sample student summary asft detect)r english Paul and Zeinab and biology Mitochondria.")

    print(detect_nonsense_words(studentText))

