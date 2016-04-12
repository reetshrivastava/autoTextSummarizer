import pyttsx
from gtts import gTTS
import os
def text_to_speech(text):
    tospeak = ""
    tospeak1 = ""
    for t in text:
        tospeak = tospeak + t.statement
    for t in tospeak:
        if t !="\'" and t !='\"' and t!="\n" and t!="[" and t!="]" and t!="\t":
            tospeak1 = tospeak1 + t
    tospeak1 = "".join(i for i in tospeak1 if ord(i)<128)
    f = open('tospeak.txt','w')
    f.write(tospeak1)
    f.close()
    f1 = open('tospeak1.txt','w')
    os.system("cat tospeak.txt | tr -d '\t\n\r' > tospeak2.txt")
    f1 = open('tospeak2.txt','r') 
    return f1.read()