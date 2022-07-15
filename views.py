from pyexpat import model
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Signup,Pro,Product
from django.db.models import Q
# Create your views here.

def searchview(request):
    q=request.GET.get('search')
    if q:
        pr=Pro.objects.filter(Q(pname__icontains=q)| Q(des__icontains=q)| Q(price__icontains=q))
        data={'p':pr}
    else:
        data={}
    return data

def hello(request):
    return HttpResponse("welcome to website")

def contact(request):
    return HttpResponse("welcome to contact page")

def signup(request):
    if request.method=='POST':
        model=Signup()
        model.fname=request.POST['fname']
        model.lname=request.POST['lname']
        model.phone=request.POST['phone']
        model.email=request.POST['email']
        model.password=request.POST['password']
        model.cpassword=request.POST['cpassword']
        model.save()
        return redirect('login')
    return render(request,'signupnew.html')

def home(request):
    if 'xyz' in request.session.keys():
        s=searchview(request)
        return render(request,'home.html',s)
    else:
        return redirect(request,'login')

def homeall(request):
    if 'xyz' in request.session.keys():
        l=Pro.objects.all()
        return render(request,'homeall.html',{'l':l})
    else:
        return redirect(request,'login')

def login(request):
    if request.method=='POST':
        try:
            m=Signup.objects.get(email=request.POST['username'])
            if m.password==request.POST['password']:
                request.session['xyz']=m.id
                print(m)
                return redirect('home')
            else: 
                return HttpResponse("Wrong Password")
        except:
            return HttpResponse("Wrong email")
    return render(request,'login.html')


def datapost(request): 
    if request.method=='POST':
        model=Product()
        model.name=request.POST['username']
        model.email=request.POST['email']
        model.save()
    return render(request,'datapost.html')
    
def productview(request,abc):
    v=Pro.objects.get(id=abc)
    return render(request,'productview.html',{'v':v})

def productdel(request,abc):
    v=Pro.objects.get(id=abc)
    v.delete()
    return redirect('proall')

def proall(request):
    if 'xyz' in request.session.keys():
        l=Pro.objects.all()
        return render(request,'homeall.html',{'l':l})
    else:
        return redirect(request,'login')
    
def logout(request):
    if 'xyz' in request.session.keys():
        del request.session['xyz']
        return redirect('login')
    else:
        return redirect('login')

def productadd(request):
    if request.method=='POST':
        model=Pro()
        model.pname=request.POST['pname']
        model.des=request.POST['des']
        model.price=request.POST['price']
        model.img=request.FILES.get('img')
        model.review=request.POST['review']
        model.save()    
        return redirect('home')
    return render(request,'productadd.html')
