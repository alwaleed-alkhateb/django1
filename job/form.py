from django import forms
from .models import apply,job

class applyform(forms.ModelForm):
    class  Meta:
        model=apply
        fields=['name','cv','web','counvert','email']
        
        
        
class JobForm(forms.ModelForm):
    class Meta:
        model=job
        fields='__all__'
        exclude=('owner','slug',)
        
        

