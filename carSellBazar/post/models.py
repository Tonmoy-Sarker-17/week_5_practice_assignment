from django.db import models
from category.models import Category
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    tittle=models.CharField(max_length=50)
    price=models.IntegerField()
    quantity=models.IntegerField() 
    category=models.ManyToManyField(Category)
    author=models.ForeignKey(User, on_delete=models.CASCADE) 
    owner=models.ManyToManyField(User,blank=True,related_name='car') 
    image= models.ImageField(upload_to='uploads/',blank=True,null=True)


    def __str__(self) -> str:
        return self.tittle
    
class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True) 

    def __str__(self) -> str:
        return f"comments by {self.name} "