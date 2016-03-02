def splitSentences(sentence):
    words = list()
    word=' '
    for c in sentence:
        word = word + c
        if c == ' ':
            word = word[:-1]
            words.append(word)
            word = ' '
    print words
    return words
            