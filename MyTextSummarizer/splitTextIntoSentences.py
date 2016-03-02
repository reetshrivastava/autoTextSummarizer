def splitText(text):
    sentences=[];
    sentence = " ";
    i = 0;
    for c in text:
        if c == '.' or c == '?' or c == '!':
            sentences.append(sentence);
            i = i+1;
            sentence = " ";
        else:
            sentence = sentence + c;
    return sentences