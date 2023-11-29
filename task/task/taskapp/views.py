
#
#
# # Create your views here.
# def home(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form= UserCreationForm()
#
#
#     return render(request,'home.html',{'form':form })
# def login(request):
#     return render(request, 'login.html')
# def new(request):
#     if request.method == 'POST':
#         form = NewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('finalpage')
#     else:
#         form= NewForm()
#     return render(request,'new.html',{'form':form })





from django.contrib import auth, messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import UserModel



def home(request):
    return render(request,"homepage.html")
def login(request):

        if request.method == 'POST':

            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('intermediate')
            else:
                messages.info(request, "invalid credential")
                return redirect('/login')
        return render(request, "login.html")
def register(request):
    if request.method== 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('login')

    else:
            form = UserCreationForm()
    return render(request,"register.html",{'form':form})
def intermediate(request):
    return render(request,"intermediate.html")

def logout(request):
        auth.logout(request)
        return redirect('/')
def drop(request):
    if request.method =='POST':
        name=request.POST['name']
        age = request.POST['age']
        dob = request.POST['dob']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        department = request.POST['department']
        course= request.POST['course']
        user=UserModel.objects.create(name=name,age=age,dob=dob,email=email,address=address,phone=phone,department=department,course=course)
        user.save()
        messages.success(request,"Done successfully!!")



    return render(request,"drop.html")






