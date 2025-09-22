from django.shortcuts import redirect, render,get_list_or_404
from networkx import reverse
from . models import job
from django.core.paginator import Paginator
from .form import applyform,JobForm



# Create your views here.

def job_list(request):
    job_list=job.objects.all()
    # https://docs.djangoproject.com/en/5.2/topics/pagination/
    #هذي عشان التنقل بين الصفحات تحت الوظايف 
    paginator = Paginator(job_list, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj}
    return render (request,'job/job_list.html',context)




def job_detail(request,slug):
    job_detail=get_list_or_404(job,slug=slug)
    
    if request.method=='POST':
        form=applyform(request.POST,request.FILES)
        if form.is_valid():
           myform= form.save(commit=False)
           myform.job=job_detail
           myform.save()    
    
    else:
        form=applyform()
    
    
    context={'job':job_detail,'form':form}
    return render(request,'job/job_detail.html',context)



def add_job(request):
    
    if request.method=='POST':
        form=JobForm(request.POST,request.FILES)
        if form.is_valid:
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save() 
            
        #return redirect(reverse('jobs:job_list'))           
            
    
    else:
        form=JobForm()
    
    
    
    return render(request,'job/add_job.html',{'form':form})
