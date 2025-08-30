from django.db import models
from django.utils.text import slugify


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
    Category=models.ForeignKey('Category',on_delete=models.CASCADE)
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