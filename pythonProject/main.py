import nonsense_detection
import profanity_detection
import foreignLang_detection

#noise threshold
threshold = 25


data = {} #return object

def detect_noise(studentText):
    cleaned_text = ""

    #calculate the total number of words in the student essay
    total_words_studentText = len(studentText.split())

    # count the total and proportion of nonsense words in the student essay
    count_nonsense_words = nonsense_detection.count_nonsense_words(studentText)
    proportion_nonsense = 0; #count_nonsense_words/total_words_studentText

    if proportion_nonsense > threshold:

        data["pre-processing_status"] = "fail"
        data["code"] = "Nonsense"
        data["cleaned_text"] = ""
        return data

    else:
        #not enough nonsense words check for profanity

        # count the total and proportion of profanity words in the student essay
        count_profanity_words = profanity_detection.count_badwords(studentText)
        proportion_profanity = count_profanity_words / total_words_studentText

        if proportion_profanity > threshold:

            data["pre-processing_status"] = "fail"
            data["code"] = "Profanity"
            data["cleaned_text"] = ""
            return data

        else:

            # not enough profanity words check for foreign language

            # check for foreign language
            isForeign = foreignLang_detection.detect_foreign_language(studentText)

            if isForeign:

                #check percentage and decide
                proportion_foreign = foreignLang_detection.proportion_foreign(studentText)

                if proportion_foreign > threshold:

                    data["pre-processing_status"] = "fail"
                    data["code"] = "Foreign"
                    data["cleaned_text"] = ""
                    return data

    # reached here, may contain some of foreign language, badwords, or nonsense words that does not pass the threshold
    # but we still want to remove them all
    cleaned_text = foreignLang_detection.remove_foreign_language(studentText)
    cleaned_text = profanity_detection.remove_badwords(cleaned_text)
    cleaned_text = nonsense_detection.remove_nonsense_words(cleaned_text)

    data["pre-processing_status"] = "success"
    data["code"] = ""
    data["cleaned_text"] = cleaned_text

    return data









def detect_relevance(cleaned_text):
    #place holder - todo
    print(cleaned_text)

if __name__ == "__main__":
    studentText = ("damn! kbjbajbd, This is an English sentence.  Another English sentence")

    print(detect_noise(studentText))
