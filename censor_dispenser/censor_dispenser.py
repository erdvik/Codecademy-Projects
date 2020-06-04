import re

def main():
    # print(censor_specific_word(email_one, 'learning algorithms'))
    # print(censor_list_of_words(email_two, proprietary_terms, True))
    # negative_words_to_censor = negative_word_limit(email_three, negative_words, 2)
    # words_to_censor = negative_words + proprietary_terms
    # print(censor_list_of_words(email_three, words_to_censor, True))

    negative_words_to_censor = negative_word_limit(email_four, negative_words, 2)
    words_to_censor = negative_words + proprietary_terms
    words_before_and_after = get_word_before_and_after(email_four, words_to_censor) 
    words_to_censor += words_before_and_after
    print(censor_list_of_words(email_four, words_to_censor, True))


# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def replace(old, new, str, caseinsentive=False):
    if caseinsentive:
        return str.replace(old, new)
    else:
        return re.sub(re.escape(old), new, str, flags=re.IGNORECASE)

def censor_specific_word(text, word, caseinsentive=False):
    num = len(word)
    replacement = ''
    for i in range(num):
        replacement += 'X'
    censored_text = replace(word, replacement, text, caseinsentive)
    return censored_text

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

def censor_list_of_words(text, words, caseinsentive=False):
    for word in words:
        text = censor_specific_word(text, word, caseinsentive)
    return text

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def negative_word_limit(text, negative_words, limit): #gets a list of negative words and a limit and returns a list of words to censor
    words_to_censor = negative_words.copy()
    empty_list = [] # to be returned if limit is not met
    count = 0
    for word in negative_words:
        if count >= limit:
            return words_to_censor
        index = text.find(word)
        if index != -1: #word is in text
            words_to_censor.remove(word)
            count += 1       
    return empty_list
        
def get_word_before_and_after(text, words):
    word_list = text.split()
    word_list = [word.strip('!.,:;+') for word in word_list]

    words_before_and_after = []

    for word in words:
        if word in word_list:
            index = word_list.index(word)
            word_before = word_list[index-1]
            words_before_and_after.append(word_before)
            word_after = word_list[index+1]
            words_before_and_after.append(word_after)

    return words_before_and_after       



    # for word in word_list:
    #     word.strip('!.,- ')
    #     if word in words:
    #         index = word_list.index(word)
    #         word_before = word_list[index-1]
    #         word_after = word_list[index+1]


if __name__ == "__main__":
    main()