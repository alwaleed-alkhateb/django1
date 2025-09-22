from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    city=models.ForeignKey('city', related_name='user_city', on_delete=models.CASCADE,blank=True,null=True)
    image_user=models.ImageField(upload_to='profile/')
    phone_number=models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.user)
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)    
    

class city(models.Model):
    name=models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.name)
    