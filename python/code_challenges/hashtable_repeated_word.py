from data_structures.hashtable import Hashtable
import re

def first_repeated_word(str):
    #clean data
    try:
        str = str.lower()
        str = re.sub(r"[\.\-\?]", "", str)
        str = re.sub(r"\W", ' ', str)
        str = str.split()
        # print(str)

        words = []
        repeated_words = []
        #check if word is in set
        for word in str:
            if word in words:
                repeated_words.append(word)
                # print(repeated_words)
            else:
                words.append(word)
                # print(words)
        return repeated_words[0]
    except:
        return None
