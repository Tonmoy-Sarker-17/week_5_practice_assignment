from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST': #user post koreche
        register_form = forms.RegistrationForm(request.POST) #user er post request data ekhane capture korlm
        if register_form.is_valid(): # post kora data gula valid kina check koreche
            register_form.save() #jodi data valid hoy taile database  e save korbo
            messages.success(request,'Account creatation successful')
            return redirect('log_in') #sob thik thkle add register ei url e pathay dibo
    
    else: #user normally website e gele blank form pabe
        register_form = forms.RegistrationForm()
    return render(request, 'register.html',{'form':register_form,'type':'Register'})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in Successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login informtion incorrect')
                return redirect('register')
        else:
            return redirect('user_login')
    else:
        form = AuthenticationForm()
        return render(request, 'register.html', {'form' : form, 'type' : 'Login'})


def pass_change(request):
    if request.method == 'POST': #user post koreche
        form = PasswordChangeForm(request.user,data=request.POST) #user er post request data ekhane capture korlm
        if form.is_valid(): # post kora data gula valid kina check koreche
            form.save() #jodi data valid hoy taile database  e save korbo
            messages.success(request,'Password update successful')
            update_session_auth_hash(request,form.user)
            return redirect('profile') #sob thik thkle add profile ei url e pathay dibo
    
    else: #user normally website e gele blank form pabe
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html',{'form':form})
def pass_change2(request):
    if request.method == 'POST': #user post koreche
        form = SetPasswordForm(request.user,data=request.POST) #user er post request data ekhane capture korlm
        if form.is_valid(): # post kora data gula valid kina check koreche
            form.save() #jodi data valid hoy taile database  e save korbo
            messages.success(request,'Password update successful')
            update_session_auth_hash(request,form.user)
            return redirect('profile') #sob thik thkle add profile ei url e pathay dibo
    
    else: #user normally website e gele blank form pabe
        form = SetPasswordForm(user=request.user)
    return render(request, 'pass_change.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.warning(request, 'Logout successful')

    return redirect('homepage')