from django.shortcuts import render, redirect
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def render_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    else:
        return render(request, "login.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)  
def perform_login(request):
    if request.method != "POST":
        return HttpResponse("Method not allowed")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_obj = authenticate(request, username=username, password=password)
        if user_obj is not None:
            login(request, user_obj)
            return HttpResponseRedirect(reverse("admin_dashboard"))
        else:
            messages.error(request, "Username or password is invalid!")
            return HttpResponseRedirect("/")

@cache_control(no_cache=True,must_revalidate=True,no_store=True) 
@login_required(login_url='/')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True) 
def perform_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('render_login'))
