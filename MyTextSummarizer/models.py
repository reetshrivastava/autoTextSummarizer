from __future__ import unicode_literals

from django.db import models


class Sentance(models.Model):
    order = models.IntegerField()
    statement=models.CharField(max_length=500)
    score=models.IntegerField()

    def __str__(self):
        return self.statement
    
class File(models.Model):
    name = models.CharField(max_length=100)
    file =  models.FileField(upload_to = u'files/toread.txt', max_length=1000)
    
class Word(models.Model):
    words=models.CharField(max_length=500)
    frequency=models.IntegerField()
    
    def __str__(self):
        return self.words