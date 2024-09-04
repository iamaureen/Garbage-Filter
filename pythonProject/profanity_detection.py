import re
from better_profanity import profanity

# text = "Crap! What a damn decision."

# censored = profanity.censor(text)
#
# print(censored)
#
#
# def is_badwords(text):
#     # Regular expression to detect the pattern "****"
#     pattern = r'\*\*\*\*'
#
#     # Search for the pattern in the text
#     if re.search(pattern, text):
#         return True  # Pattern detected
#     else:
#         return False  # Pattern not detected
#


def count_badwords(text):
    """
    Count the number of occurrences of '****' in the text.
    """
    censored = profanity.censor(text)
    return len(re.findall(r'\*\*\*\*', censored))

def remove_badwords(text):
    """
    Replace all occurrences of '****' in the text with an empty string.
    """
    censored = profanity.censor(text)
    return re.sub(r'\*\*\*\*', '', censored)




