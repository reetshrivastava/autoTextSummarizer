from stop_words import get_stop_words
from MyTextSummarizer.splitTextIntoSentences import splitText
from MyTextSummarizer.models import Word
from MyTextSummarizer.CountFrequency import  setfrequency
from MyTextSummarizer.splitSentencesIntoWords import splitSentences
import datetime
from nltk import PorterStemmer
from django.core.exceptions import ObjectDoesNotExist
class Sentances():
    def __init__(self,order,statement,score):
        self.order = order
        self.statement= statement
        self.score = score
        
    def getKey(self):
        return self.score
    
    def getorderkey(self):
        return self.order
        
def summary(text,depth):
    print "enter summary:"
    print  datetime.datetime.time(datetime.datetime.now())
    print "\n"
    original_word_count = 0
    summary_word_count = 0
    params = dict();
    order = 1
    sentences_to_save = list()
    stop_words = get_stop_words('en')
    sentences = splitText(text);
    sentence_count = len(sentences)
    setfrequency(text)
    print "loop1:"
    print  datetime.datetime.time(datetime.datetime.now())
    print "\n"
    for s in sentences:
        k = Sentances(statement=s,score=0,order=0)
        sentences_to_save.append(k)
    print "loop1end:"
    print  datetime.datetime.time(datetime.datetime.now())
    print "\n"         
    for s in sentences_to_save:
        totalscore = 0
        swords = s.statement.split()
        for sw in swords:
            sw1=""
            original_word_count = original_word_count + 1
            sw = sw.lower()
            sw = PorterStemmer().stem_word(sw)
            for c in sw:
                if c == "." or c == "," or c == ":" or c=="(" or c==")" :
                    continue
                else:
                    sw1 = sw1 + c
            flag = 0
            for stopw in stop_words:
                if sw == stopw:
                    flag = 1;
                    break;
            if flag == 0:
                #score = countfrequency(sw,text)
                try:
                    score = (Word.objects.get(words = sw1)).frequency
                except ObjectDoesNotExist:
                    continue
                totalscore+=score
        s.score = totalscore
        s.order = order
        order = order + 1
    print "loop2end:"
    print  datetime.datetime.time(datetime.datetime.now())
    print "\n"
    order_sentences = sorted(sentences_to_save,key=Sentances.getKey,reverse=True)
    s = 0
    important_sentences = list()
    print "loop3:"
    print  datetime.datetime.time(datetime.datetime.now())
    print "\n"
    while(s < sentence_count/(100/depth)):
        important_sentences.append(order_sentences[s])
        summary_word_count = summary_word_count + len(splitSentences(order_sentences[s].statement))
        s = s + 1
    print "loop3end:"
    print  datetime.datetime.time(datetime.datetime.now())
    print "\n"
    ordered_important_sentences = sorted(important_sentences,key=Sentances.getorderkey)
    params["summary"]=ordered_important_sentences
    params["originalcount"] = original_word_count
    params["summarycount"] = summary_word_count
    Word.objects.all().delete()
    return params