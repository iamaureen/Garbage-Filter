import re
from better_profanity import profanity

text = "Crap! What a mother fucking decision."

censored = profanity.censor(text)

print(censored)


def is_badwords(text):
    # Regular expression to detect the pattern "****"
    pattern = r'\*\*\*\*'

    # Search for the pattern in the text
    if re.search(pattern, text):
        return True  # Pattern detected
    else:
        return False  # Pattern not detected


# # Test the function with example paragraphs
# paragraph_1 = "This is a sample text with **** in it."
# paragraph_2 = "This is a clean text without the pattern."

# Check the paragraphs
flag_1 = is_badwords(censored)
print(f"Paragraph contains '****': {flag_1}")

def count_badwords(text):
    """
    Count the number of occurrences of '****' in the text.
    """
    return len(re.findall(r'\*\*\*\*', text))

def replace_badwords(text):
    """
    Replace all occurrences of '****' in the text with an empty string.
    """
    return re.sub(r'\*\*\*\*', '', text)

# Test the functions with an example paragraph
paragraph = censored

# Count the occurrences of '****'
count = count_badwords(paragraph)
print(f"Number of occurrences of '****': {count}")

# Replace the occurrences of '****'
cleaned_text = replace_badwords(paragraph)
print(f"Text after replacing '****': {cleaned_text}")



