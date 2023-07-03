from django import forms
from .models import Testimonials
from .models import Blog


class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100,)
    message = forms.CharField(widget=forms.Textarea)


#testimonials  

class TestimonialForm(forms.ModelForm):
    class Meta:
        model= Testimonials
        fields = ['name','company','paragraph','image']


#testimonials end

  
#blog

class BlogForm(forms.ModelForm):
    class Meta:
        model= Blog
        fields = ['heading','paragraph','image',] 

#blog end

#admin form




