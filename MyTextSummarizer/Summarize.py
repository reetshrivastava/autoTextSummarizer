from stop_words import get_stop_words
from MyTextSummarizer.splitTextIntoSentences import splitText
from MyTextSummarizer.models import Sentance
from MyTextSummarizer.CountFrequency import countfrequency
def summary(text):
    params = dict();
    order = 1
    stop_words = get_stop_words('en')
    sentences = splitText(text);
    for s in sentences:
        s = Sentance(statement = s.encode('utf-8'),score = 0,order=0)
        s.save()
    slist = Sentance.objects.all()
    for s in slist:
        totalscore = 0
        swords = s.statement.split()
        for sw in swords:
            sw = sw.lower()
            flag = 0
            for stopw in stop_words:
                if sw == stopw:
                    flag = 1;
                    break;
            if flag == 0:
                score = countfrequency(sw,text)
                totalscore+=score
        s.score = totalscore
        s.order = order
        order = order + 1
        s.save()
    out_sentences = Sentance.objects.order_by("-score")[:2]
    out_sentences_list = list()
    for os in out_sentences:
        out_sentences_list.append(os.statement)
    i = 0
    lowest_object = list()
    while(i<2):
        lowest = 999
        for os in out_sentences_list:
            o = Sentance.objects.get(statement = os)
            if o.order < lowest:
                lowest = o.order
        ho = Sentance.objects.get(order = lowest)  
        lowest_object.append(ho)
        out_sentences_list.remove(ho.statement)
        i = i + 1
    params["summary"] = lowest_object
    Sentance.objects.all().delete()
    return params