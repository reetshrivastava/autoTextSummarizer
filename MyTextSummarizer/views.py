from django.http.response import HttpResponse
from django.shortcuts import render
from MyTextSummarizer.Summarize import summary
from MyTextSummarizer.models import File



def index(request):
    return render(request,'index.html')


def fileupload(request):
    # Handle file upload
    print "oley"
    f = File(name = 'filename',file = request.FILES['myfile'])
    f.save()
    filename = request.FILES['myfile'].name
    f = open('files/toread.txt/'+filename,'r')
    params = summary(f.read())
    File.objects.all().delete()
    return render(request,'summary.html',params)


def summarize(request):
    text = request.POST.get('text')
    params = summary(text)
    return render(request,'summary.html',params)