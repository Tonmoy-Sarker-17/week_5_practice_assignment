from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import DetailView

# Create your views here.
@login_required
def add_post(request):
    
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author=request.user
            post_form.save()
            return redirect('add_post')
    
    else:
        post_form = forms.PostForm()
    return render(request, 'add_carPost.html',{'form':post_form})

@login_required
def edit_post(request,id):
    post=models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST,instance=post)
        if post_form.is_valid():
            post_form.instance.author=request.user
            post_form.save()
            return redirect('homepage')
    
    
    return render(request, 'add_carPost.html',{'form':post_form})

@login_required
def delete_post(request,id):
    post=models.CarPost.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

class DetailPostView(DetailView):
    model=models.Post
    template_name='post_details.html'
    pk_url_kwarg='id'

    def post(self,request, *args,**kwargs):
        comment_form=forms.CommentForm(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
        return self.get(request, *args,**kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post=self.object
        comments=post.comments.all()
        comment_form=forms.CommentForm()
        
        context['comments']=comments
        context['comment_form']=comment_form
        return context



@login_required
def buy(request, id):
    car = models.Post.objects.get(pk=id)

    if car.owner.filter(pk=request.user.id).exists():
        messages.warning(request, "You already own this car")
    else:
        if car.quantity > 0:
            car.owner.add(request.user)
            car.quantity -= 1
            car.save()
            messages.success(request, "You have successfully purchased this car!")
            return redirect('homepage')
        else:
            messages.error(request, "This car is no longer available")
        return redirect('detail_post', id=id) 

    return redirect('homepage')