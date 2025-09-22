from django.shortcuts import redirect, render
from .forms import singupform
from django.contrib.auth import authenticate,login
from .models import Profile
# Create your views here.




def signup(request):
    if request.method=='POST':
        form=singupform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
            
    else:
        form=singupform()
        
    
    return render(request,'registration/singup.html',{'form':form})


def profile(requset):
    profile=Profile.objects.get(user=requset.user)
    
    return render(requset,'registration/profile.html',{'profile':profile})


def profile_edit(requset):
    
    
    return render(requset,'registration/profile_edit.html',{'profile':profile})

    