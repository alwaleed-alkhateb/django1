from django.db import models

JOB_TYPE=(('FULL TIME','FULL TIME'),('PART TIME','PART TIME'))

# Create your models here.
class job(models.Model):
    title=models.CharField(max_length=50)
    #loction
    job_type=models.CharField(max_length=50,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)  
    published=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salry=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    
    def __str__(self):
        return self.title
    