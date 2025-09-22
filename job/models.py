from collections import UserDict
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


JOB_TYPE=(('FULL TIME','FULL TIME'),('PART TIME','PART TIME'))

# Create your models here.
class job(models.Model):
    owner=models.ForeignKey(User, verbose_name=("job_owner"), on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    #loction
    job_type=models.CharField(max_length=50,choices=JOB_TYPE,default=1)
    description=models.TextField(max_length=1000)  
    published=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    salry=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    Category=models.ForeignKey('Category',on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='jobs/')
    
    slug=models.SlugField(blank=True,null=True)
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)  
        super(job,self).save(*args, **kwargs)
        

    
    
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name=models.CharField(max_length=25)
    
    
    def __str__(self):
        return self.name
    
    
class apply(models.Model):
    
    job=models.ForeignKey(job, related_name=("apply_job"), on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    email=models.EmailField(max_length=100)
    web=models.URLField()
    cv=models.FileField(upload_to='apply/', max_length=100)
    counvert=models.CharField( max_length=500)
    
    def __str__(self):
        return self.name
    