from nltk import PorterStemmer
def countfrequency(word,text):
    frequency = 0
    word = PorterStemmer().stem_word(word)
    list_of_words = text.split()
    for l in list_of_words:
        if PorterStemmer().stem_word(word) == PorterStemmer().stem_word(l.lower()) or PorterStemmer().stem_word(word)+'.' == PorterStemmer().stem_word(l.lower()):
            frequency = frequency + 1
    return frequency
            