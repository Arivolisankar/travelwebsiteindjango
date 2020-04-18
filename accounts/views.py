from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect ('/')


def register(request):
    if request.method=='POST':
        first_name=request.POST['txtFirst']
        last_name=request.POST['txtLast']
        username=request.POST['txtUname']
        email=request.POST['txtEmail']
        password=request.POST['txtPass']
        cpassword=request.POST['txtCpass']

        if password==cpassword:
            if User.objects.filter(username=username).exists(): 
                messages.info(request,'Name already taken !!')
                return redirect('register')
                

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken !!')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'User Created !!')
                return redirect('login')
        else:
            messages.info(request,'Passwords do not match !!')
            return redirect('register')
        return redirect('/')


    else:
        return render(request,'register.html')



def login(request):
    if request.method=='POST':
        username=request.POST['txtUname']
        password=request.POST['txtPass']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect ('/')
        else:
            messages.info(request,'Invalid Credentials!!')
            return redirect ('login.html')


    else:
        return render(request,'login.html')
