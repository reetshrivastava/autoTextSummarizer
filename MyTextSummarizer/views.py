from MyTextSummarizer.Summarize import summary
from MyTextSummarizer.models import File
import pytesseract
from PIL import Image
import string
from django.shortcuts import render
from django.http.response import HttpResponse


def downloadfile(request):
    f = open('tospeak.txt','r')
    data = f.read()
    response = HttpResponse(data,content_type='text/plain')
    response['Content-Disposition'] = 'attachment;filename="Summary"'
    return response

def index(request):
    return render(request,'index.html')

def imageupload(request):
    # Handle image upload
    depth = request.POST.get('range')
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
    params = summary(text,float(depth))
    File.objects.all().delete()
    return params
    

def fileupload(request):
    # Handle file upload
    depth = request.POST.get('range')
    f = File(name = 'filename',file = request.FILES['myfile'])
    f.save()
    filename = request.FILES['myfile'].name
    f = open('files/toread.txt/'+filename,'r')
    params = summary(f.read(),float(depth))
    File.objects.all().delete()
    return params


def summarize(request):
    button = request.POST.get('button')
    if button == "Upload File":
        params = fileupload(request)
    elif button == "Upload Image":
        params = imageupload(request)
    else:
        text = request.POST.get('text')
        depth = request.POST.get('range')
        params = summary(text,float(depth))
    
    return render(request,'summary.html',params)