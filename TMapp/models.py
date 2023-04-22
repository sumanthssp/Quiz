from django.db import models

# Create your models here.
class Questions(models.Model):
    no=models.IntegerField(null=True)
    qsn=models.CharField(max_length=100)
    o1=models.CharField(max_length=50)
    o2=models.CharField(max_length=50)
    o3=models.CharField(max_length=50)
    o4=models.CharField(max_length=50)
    ans=models.CharField(max_length=50)

class Score(models.Model):
    tname=models.CharField(max_length=50)
    m1=models.CharField(max_length=50)
    m2=models.CharField(max_length=50)
    score=models.CharField(max_length=40)
    time=models.CharField(max_length=20,null=True)

