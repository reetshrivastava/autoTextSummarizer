from nltk import PorterStemmer
from MyTextSummarizer.models import Word
from django.core.exceptions import MultipleObjectsReturned

class Words():
    def __init__(self,word,frequency):
        self.word = word
        self.frequency= frequency
        
def countfrequency(word,text):
    frequency = 0
    word = PorterStemmer().stem_word(word)
    list_of_words = text.split()
    for l in list_of_words:
        if PorterStemmer().stem_word(word) == PorterStemmer().stem_word(l.lower()) or PorterStemmer().stem_word(word)+'.' == PorterStemmer().stem_word(l.lower()):
            frequency = frequency + 1
    return frequency
            
def setfrequency(text):
    words_list = list()
    w_to_save = list()
    list_of_words = text.split()
    for l in list_of_words:
        l = PorterStemmer().stem_word(l)
        l = l.lower()
        l1=""
        for c in l:
            if c == "." or c == "," or c == ":" or c=="(" or c==")" :
                continue
            else:
                l1 = l1 + c
        if l1 in words_list:
            for q in w_to_save:
                    if q.words == l1:
                        q.frequency = q.frequency + 1
        else:
            w = Word(words = l1,frequency =1)
            w_to_save.append(w)
            words_list.append(l1)
    Word.objects.bulk_create(w_to_save)       