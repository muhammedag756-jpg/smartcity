from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
# Create your views here.
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import Group, User

from myapp.models import *
def index(request):
    return   render(request,"index.html")

  
def login_get(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            if user.groups.filter(name='Admin').exists():
                login(request,user)
                return redirect('/myapp/admin_home/')
            if user.groups.filter(name='Authority').exists():
                login(request,user)
                return redirect('/myapp/authority_home/')
            if user.groups.filter(name='User').exists():
                login(request,user)
                return redirect('/myapp/user_home/')
            
            
            
            else:
                return redirect('/myapp/login_get/')
    return render(request,'login.html')
                
            
        
        
        


def admin_addauthority(request):
 
    if request.method == 'POST':
        name=request.POST['name']
        type=request.POST['type']
        phone=request.POST['phone']
        email=request.POST['email']
        username=request.POST['username']
        passwrord=request.POST['password']
        
        user=User.objects.create_user(username=username,password=passwrord)
        user.save()
        user.groups.add(Group.objects.get(name="Authority"))
        a=authority()
        a.name=name
        a.type=type
        a.phone=phone
        a.email=email
        a.LOGIN=user
        a.save()
        return HttpResponse('''<script>alert("added successfully");window.location='/myapp/admin_viewauthority/'</script>''')
        
        
    
    return render(request,"admin/add authority.html")
def admin_assignauthority(request,id):
    data=authority.objects.all()
    if request.method == 'POST':
        a=assign_authority()
        a.status='assigned'
        a.date=datetime.now().today()
        a.REQUEST_id=id
        a.AUTHORITY_id=request.POST['authority']
        a.save()
        return HttpResponse('ok')
    return render(request,"admin/assign authorit.html",{'data': data})

def admin_authorityfeedback(request):
    return render(request,"admin/authority feedback.html")

def admin_edit(request,id):
    o=authority.objects.get(id=id)
    if request.method == 'POST':
        o.name=request.POST.get("name")
        o.type=request.POST.get('type')
        o.phone=request.POST.get('phone')
        o.email=request.POST.get('email')
        o.save()
        return HttpResponse('''<script>alert("edited succesfuly");window.location='/myapp/admin_viewauthority/'</script>''')   
    return render(request,"admin/edit authority.html",{"data":o})
def delete_authority(request,id):
    a=authority.objects.get(id=id)
    a.delete()
    return HttpResponse('''<script>alert("deleted succesfuly");window.location='/myapp/admin_viewauthority/'</script>''') 

def admin_verify(request):
    u=user_table.objects.all()
    return render(request,"admin/verify user.html",{"data":u})

def accept_user(request,id):
    user_table.objects.filter(id=id).update(status="accepted")
    return HttpResponse('''<script>alert("accepted succesfuly");window.location='/myapp/admin_verify/'</script>''')
def reject_user(request,id):
    user_table.objects.filter(id=id).update(status="rejected")
    return HttpResponse('''<script>alert("accepted succesfuly");window.location='/myapp/admin_verify/'</script>''')


def admin_view(request,):
    a=assign_authority.get()
    return render(request,"admin/view assignment.html",{"data":a})
def admin_viewauthority(request):
    a=authority.objects.all()
    
    return render(request,"admin/view authority.html",{"data":a})
def admin_viewreq(request):
    u=request_table.objects.all()
    
    return render(request,"admin/view user req.html",{"data":u})


def authority_updatestat(request):
    if request.method == 'POST':
        status=request.POST['status']
        s=assign_authority()
        s.status=status
        s.save()
        return HttpResponse('ok')    
    return render(request,"authority/update status.html")
def authority_viewissues(request):
    a=assign_authority.objects.filter(AUTHORITY__LOGIN=request.user) 
    return render(request,"authority/view assigned issues.html",{"data":a})
def authority_viewfeed(request):
    a=feedback.objects.all
    return render(request,"authority/view feedback.html",{"data":a})


def user_register(request):
     if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        photo=request.FILES['photo']
        ward=request.POST['ward']
        place=request.POST['place']
        pin=request.POST['pin']
        post=request.POST['post']
      
        
        user=User.objects.create_user(username=username,password=password)
        user.save()
        user.groups.add(Group.objects.get(name="User"))
        u=user_table()
        u.name=name
        u.phone=phone
        u.email=email
        u.image=photo
        u.ward=ward
        u.place=place
        u.pin=pin
        u.post=post
        u.LOGIN=user
        u.type=type
        u.save()
        return HttpResponse('''<script>alert("added succesfully");window.location='/myapp/login_get/'</script>''')
     return render(request,"user/register.html")
 
def user_sendfeedback(request):
    if request.method == 'POST':
        feedback=request.POST['feedback']
        rating=request.POST['rating']
        feed=feedback()
        feed.feedback=feedback
        feed.rating=rating
        feed.date=datetime.now().today()
        feed.ASSIGN_id=authority.objects.get(id=id)
        feed.USER=user_table.objects.get(LOGIN_id=request.user.id)
        feed.save()
        return HttpResponse(''' <script>alert("send sucessfully");window.location='/myapp/user_viewfeedback/' </script>''')
        
    return render(request,"user/send feedback.html")
def user_sendreq(request):
     if request.method == 'POST':
        title=request.POST['title']
        description=request.POST['description']
        image=request.FILES['image']
        req=request_table()
        req.USER=user_table.objects.get(LOGIN=request.user)
        req.title=title
        req.status='send'
        req.descreption=description
        req.image=image
        req.date=datetime.now().today()
        req.save()
        
        return HttpResponse('''<script>alert(" req send sucessfully");window.location='/myapp/user_requeststat/'</script>''')
    
    
     return render(request,"user/send req.html")
def user_viewassigned(request,id):
    a=assign_authority.objects.filter(REQUEST_id=id)
    
    return render(request,"user/view assigned.html",{"data":a})
def user_viewfeedback(request):
    a=feedback.objects.all
    return render(request,"user/view feedback.html",{"data":a})
def user_requeststat(request):
    
     u=request_table.objects.all()
     return render(request,"user/view request status.html",{"data":u})
def admin_home(request):
    return render(request,"admin/admin home.html")
def authority_home(request):
    return render(request,"authority/authority home.html")
def user_home(request):
    return render(request,"user/user home.html")

def assigned_details(request):
    a=assign_authority.objects.all()
    return render(request,"admin/assigned view.html",{"data":a})