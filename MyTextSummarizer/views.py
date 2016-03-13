from django.http.response import HttpResponse
from MyTextSummarizer.Summarize import summary
from MyTextSummarizer.models import File
import pytesseract
from PIL import Image
import string
from django.shortcuts import render
import datetime



def index(request):
    return render(request,'index.html')

def imageupload(request):
    # Handle image upload
    new_filename = ""
    f = File(name = 'filename',file = request.FILES['myfile'])
    f.save()
    filename = request.FILES['myfile'].name
    for i in filename:
        if i == " ":
            new_filename = new_filename + "_"
        elif i == ":":
            continue
        else:
            new_filename = new_filename + i         
    print filename
    text = pytesseract.image_to_string(Image.open('files/toread.txt/'+new_filename))
    printable = set(string.printable)
    text = filter(lambda x:x in printable,text)
    print text  
    params = summary(text)
    File.objects.all().delete()
    return render(request,'summary.html',params)
    

def fileupload(request):
    # Handle file upload
    f = File(name = 'filename',file = request.FILES['myfile'])
    f.save()
    filename = request.FILES['myfile'].name
    f = open('files/toread.txt/'+filename,'r')
    params = summary(f.read())
    File.objects.all().delete()
    return render(request,'summary.html',params)


def summarize(request):
    print "start time:"
    print  datetime.datetime.time(datetime.datetime.now())
    print "\n"
    text = request.POST.get('text')
    depth = request.POST.get('range')
    params = summary(text,float(depth))
    
    return render(request,'summary.html',params)