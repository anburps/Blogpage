from os import login_tty
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from apps.forms import LoginForm, contactForm
from .models import Blogs, Contact
from .models import Category, Photo

from django.contrib.auth.decorators import login_required

import random
import string




@login_required
def home(request):
    return render(request,'home.html')



@login_required
def contact_us(request):
    if request.method=="POST":
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        fphone=request.POST.get("phone")
        fdesc=request.POST.get("desc")
        query=Contact(name=fname,email=femail, phonenumber=fphone,description=fdesc) 
        query.save()
        return redirect('contact_us')
    
    return render(request,'contact.html')
@login_required
def about(request):
    return render(request,'about.html')
@login_required
def services(request):
    contacts=Contact.objects.all()
    search_query = request.GET.get('search', '')

    
    contact_list = Contact.objects.filter(name__icontains=search_query)

   
   
    
   

    paginator = Paginator(contact_list, 4)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
       
        contacts = paginator.page(1)
    except EmptyPage:
         
        contacts = paginator.page(paginator.num_pages)

    context = {
        'contacts':contacts,
        
        'search_query': search_query,
        
    }
    return render(request,'services.html',context)
@login_required
def blog(request):
    allposts=Blogs.objects.all()
   
    return render(request,'blog.html')




def handlesLogin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            captcha_response = form.cleaned_data['captcha']

            # Validate CAPTCHA
            if not captcha_response:
                messages.error(request, "CAPTCHA is required.")
                return redirect("handlesLogin")

            # Authenticate user with username and password
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, "Invalid credentials.")
                return redirect("handlesLogin")

            # Login the user
            login(request, user)
            messages.success(request, "Login Success")
            return redirect("home")
    else:
        form = LoginForm()
         
    return render(request, 'Login.html', {'form': form})
def Logout(request):
    logout(request)
    messages.info(request,'Logout success')
    return redirect("handlesLogin")

def HandlesSignup(request):
    if request.method=='POST':
        name=request.POST.get("UserName")
        email=request.POST.get("email")
        password=request.POST.get("pass1")
        confirmpassword=request.POST.get("pass2")
        if password!=confirmpassword:
            messages.warning(request,"password is incorrect")
            return redirect("HandlesSignup")
        try:
            if User.objects.get(username=name):
                 messages.info(request,"UserName Is Taken")
                 return redirect("HandlesSignup")
        except:
            pass

        try:
            if User.objects.get(username=name):
                 messages.info(request,"Email Is Taken")
                 return redirect("HandlesSignup")
        except:
            pass
        myuser=User.objects.create_user(name,email,password)
        myuser.save()
        messages.info(request,"Signup Success please Login.")
        return redirect("handlesLogin")
    return render(request,'Signup.html')



@login_required(login_url='login')
def gallery(request):
    user = request.user
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(category__user=user)
    else:
        photos = Photo.objects.filter(
            category__name=category, category__user=user)

    categories = Category.objects.filter(user=user)
    context = {'categories': categories, 'photos': photos}
    return render(request, 'gallery.html', context)


@login_required(login_url='login')
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {'photo': photo})


@login_required(login_url='login')
def addPhoto(request):
    user = request.user

    categories = user.category_set.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                user=user,
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'add.html', context)