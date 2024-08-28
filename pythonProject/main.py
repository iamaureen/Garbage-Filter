import nonsense_detection
import profanity_detection
import foreignLang_detection

#noise threshold
threshold = -1

cleaned_text = ""

def detect_noise(studentText):

    #calculate the total number of words in the student essay
    total_words_studentText = len(studentText.split())

    # count the total and proportion of nonsense words in the student essay
    count_nonsense_words = nonsense_detection.count_nonsense_words(studentText)
    proportion_nonsense = count_nonsense_words/total_words_studentText

    if proportion_nonsense > threshold:
        #todo: return a dict
        return "{'pre-processing-status': 'fail', 'code':'Nonsense', 'cleaned_text':''}"
    else:
        #clean text
        cleaned_text = nonsense_detection.remove_nonsense_words(studentText)

        # count the total and proportion of profanity words in the student essay
        count_profanity_words = profanity_detection.count_badwords(studentText)
        proportion_profanity = count_profanity_words / total_words_studentText

        if proportion_profanity > threshold:
            # todo: return a dict
            return "{'pre-processing-status': 'fail', 'code':'profanity', 'cleaned_text':''}"
        else:
            #clean text
            cleaned_text = profanity_detection.replace_badwords(cleaned_text)

            # check for foreign language
            #todo how to calculate the proportion (sentence wise?)
            isForeign = foreignLang_detection.detect_foreign_language(studentText)

            if isForeign:
                # todo: return a dict
                return "{'pre-processing-status': 'fail', 'code':'profanity', 'cleaned_text':''}"
            else:
                #clean text: remove the foreign words
                clean_text = ""
                # todo: return a dict
                return "{'pre-processing-status': 'success', 'code':'', 'cleaned_text':"+cleaned_text+"}"



def detect_relevance(cleaned_text):
    #place holder - todo
    print(cleaned_text)

if __name__ == "__main__":
    studentText = ("This is a sample student summary kbbggooo lkasokokd damn Zeinab and Paul. "
                   "we want to detect noise present in this text."
                   "это компьютерный портал для гиков")

    print(type(detect_noise(studentText)))
    detect_relevance(cleaned_text)