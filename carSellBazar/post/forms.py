from django import forms
from .models import CarPost,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = CarPost
        exclude=['author']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['name','email','body']
  