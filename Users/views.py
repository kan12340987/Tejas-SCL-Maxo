from django.shortcuts import render, redirect
from django.contrib import messages
import Users.forms
from webapp import views as web_views
from .forms import SignUpForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

def login(request):
    signupform = SignUpForm(request.POST)
    login_form = AuthenticationForm(data=request.POST)

    if request.method == 'POST':

            if signupform.is_valid():
                signupform.save()
                return redirect('Users-Homepage')

            elif login_form.is_valid():
                user_cred = request.POST['username']
                pwd = request.POST['password']
                user = authenticate(request, username=user_cred, password=pwd)
                if user is not None:
                    auth_login(request, user)
                    messages.success(request, f'You have logged into your account { user_cred } !!')
                    return redirect('Users-Homepage')
                else:
                    messages.error(request, f'Invalid Credentials')
                    return HttpResponseRedirect("")

            else:
                print('error')
                messages.error(request, f'Invalid Credentials')
                return HttpResponseRedirect(request.path_info)


    else:    
        signupform = SignUpForm()
    context = {
        'form': signupform,
        'login_form': login_form,
    }
    return render(request, 'login_form.html', context)

@login_required
def logOut(request):
    logout(request)
    return redirect(web_views.home)

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def contact(request):
    return render(request,'contact.html')    

