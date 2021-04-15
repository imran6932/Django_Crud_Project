from django.shortcuts import render, HttpResponseRedirect
from .forms import Signup_form, Login_form, Student
from django.contrib.auth import authenticate, login, logout
from .models import Student_user
from django.contrib import messages


# Create your views here.
# delete
def delete_data(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Student_user.objects.get(pk=id)
            pi.delete()
            messages.warning(request, 'Post Deleted Successfully.')
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
    
# Home
def home(request):
    return render(request, 'student/home.html')

#signup
def signup(request):
    if request.method == 'POST':
        form = Signup_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account created successfully')
            form = Signup_form()
    else:
        form = Signup_form()
    return render(request, 'student/signup.html', {'form':form})

#login
def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = Login_form(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'you have logged in successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = Login_form()
        return render(request, 'student/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

        

#logout
def logout_user(request):
    logout(request)
    messages.success(request, 'You have logged out successfully')
    return HttpResponseRedirect('/')

#dashboard
def dashboard(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = Student(request.POST)
            if form.is_valid():
                form.save()
                form = Student()
                messages.success(request, 'Student Added Successfully')
        else:
            form = Student()
        stu = Student_user.objects.all()
        return render(request, 'student/dashboard.html', {'form':form, 'fm':stu})
    else:
        return HttpResponseRedirect('/login/')

#update
def update_data(request, id):
    if request.method == 'POST':
        pi = Student_user.objects.get(pk=id)
        fm = Student(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Form updated Successfully')
            
    else:
        pi = Student_user.objects.get(pk=id)
        fm = Student(instance=pi)
    return render(request, 'student/update.html', {'form':fm})

