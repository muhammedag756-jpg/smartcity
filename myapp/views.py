from datetime import date

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import Group, User

from myapp.models import *


def _alert(message, redirect_url):
    return HttpResponse(
        f'''<script>alert("{message}");window.location="{redirect_url}"</script>'''
    )


def _get_user_profile(user):
    return get_object_or_404(user_table, LOGIN=user)


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
                profile = user_table.objects.filter(LOGIN=user).first()
                if profile is None:
                    return _alert("User profile not found", "/myapp/login_get/")
                if profile.status == "blocked":
                    return _alert(
                        "Your account is blocked by admin.",
                        "/myapp/login_get/",
                    )
                if profile.status != "accepted":
                    return _alert(
                        f"Your account is {profile.status}. Please wait for admin approval.",
                        "/myapp/login_get/",
                    )
                login(request,user)
                return redirect('/myapp/user_home/')
            
            
            
            else:
                return redirect('/myapp/login_get/')
        return _alert("Invalid username or password", "/myapp/login_get/")
    return render(request,'login.html')
                
            
        
        
        


def admin_addauthority(request):
 
    if request.method == 'POST':
        name=request.POST['name']
        type=request.POST['type']
        phone=request.POST['phone']
        email=request.POST['email']
        username=request.POST['username']
        passwrord=request.POST['password']

        if User.objects.filter(username=username).exists():
            return _alert("Username already exists", "/myapp/admin_addauthority/")
        
        group, _ = Group.objects.get_or_create(name="Authority")
        user=User.objects.create_user(username=username,password=passwrord)
        user.save()
        user.groups.add(group)
        a=authority()
        a.name=name
        a.type=type
        a.phone=phone
        a.email=email
        a.LOGIN=user
        a.save()
        return _alert("added successfully", "/myapp/admin_viewauthority/")
        
        
    
    return render(request,"admin/add authority.html")
def admin_assignauthority(request,id):
    req = get_object_or_404(request_table, id=id)
    data=authority.objects.all()
    if request.method == 'POST':
        authority_id = request.POST['authority']
        a, _ = assign_authority.objects.update_or_create(
            REQUEST=req,
            defaults={
                "AUTHORITY_id": authority_id,
                "status": "assigned",
                "date": date.today(),
            },
        )

        req.status = a.status
        req.save()
        return _alert("Authority assigned successfully", "/myapp/admin_view_assign/")
    return render(request,"admin/assign authorit.html",{'data': data, 'issue': req})

def admin_authorityfeedback(request):
    data = feedback.objects.select_related(
        "ASSIGN__AUTHORITY", "ASSIGN__REQUEST", "USER"
    ).order_by("-date")
    return render(request,"admin/authority feedback.html", {"data": data})

def admin_authorityfeedbackwithid(request,id):
    data = feedback.objects.filter(ASSIGN__AUTHORITY_id=id)
    return render(request,"admin/authority_feedback_withid.html", {"data": data})


def admin_edit(request,id):
    o=authority.objects.get(id=id)
    if request.method == 'POST':
        o.name=request.POST.get("name")
        o.type=request.POST.get('type')
        o.phone=request.POST.get('phone')
        o.email=request.POST.get('email')
        o.save()
        return _alert("edited succesfuly", "/myapp/admin_viewauthority/")   
    return render(request,"admin/edit authority.html",{"data":o})
def delete_authority(request,id):
    a=authority.objects.select_related("LOGIN").get(id=id)
    login_user = a.LOGIN
    a.delete()
    login_user.delete()
    return _alert("deleted succesfuly", "/myapp/admin_viewauthority/") 

def admin_verify(request):
    u=user_table.objects.all()
    return render(request,"admin/verify user.html",{"data":u})

def accept_user(request,id):
    user_table.objects.filter(id=id).update(status="accepted")
    return _alert("accepted succesfuly", "/myapp/admin_verify/")
def reject_user(request,id):
    user_table.objects.filter(id=id).update(status="rejected")
    return _alert("rejected succesfuly", "/myapp/admin_verify/")
def block_user(request,id):
    user_table.objects.filter(id=id, status="accepted").update(status="blocked")
    return _alert("blocked succesfuly", "/myapp/admin_verify/")
def unblock_user(request,id):
    user_table.objects.filter(id=id, status="blocked").update(status="accepted")
    return _alert("unblocked succesfuly", "/myapp/admin_verify/")


def admin_view_assign(request):
    a=assign_authority.objects.select_related("REQUEST", "AUTHORITY").all().order_by("-date")
    return render(request,"admin/view assignment.html",{"data":a})
def admin_viewauthority(request):
    a=authority.objects.all()
    
    return render(request,"admin/view authority.html",{"data":a})
def admin_viewreq(request):
    u=request_table.objects.select_related("USER").all().order_by("-date")
    
    return render(request,"admin/view user req.html",{"data":u})


def authority_updatestat(request,id):
    authority_data = authority.objects.get(LOGIN=request.user)
    assignment = assign_authority.objects.get(id=id, AUTHORITY=authority_data)
    if request.method == 'POST':
        status=request.POST['status']
        assignment.status=status
        assignment.save()
        assignment.REQUEST.status=status
        assignment.REQUEST.save()
        return _alert("Status updated successfully", f"/myapp/authority_viewissues/?status={status}")    
    return render(request,"authority/update status.html", {"data": assignment})

def authority_markongoing(request,id):
    authority_data = authority.objects.get(LOGIN=request.user)
    assignment = assign_authority.objects.get(id=id, AUTHORITY=authority_data)
    assignment.status = "ongoing"
    assignment.save()
    assignment.REQUEST.status = "ongoing"
    assignment.REQUEST.save()
    return _alert("Marked as ongoing", "/myapp/authority_viewissues/?status=ongoing")

def authority_markcompleted(request,id):
    authority_data = authority.objects.get(LOGIN=request.user)
    assignment = assign_authority.objects.get(id=id, AUTHORITY=authority_data)
    assignment.status = "completed"
    assignment.save()
    assignment.REQUEST.status = "completed"
    assignment.REQUEST.save()
    return _alert("Marked as completed", "/myapp/authority_viewissues/?status=completed")

def authority_viewissues(request):
    authority_data = authority.objects.get(LOGIN=request.user)
    status = request.GET.get("status", "all")

    a = assign_authority.objects.filter(AUTHORITY=authority_data).order_by("-date")
    if status in ["assigned", "ongoing", "completed"]:
        a = a.filter(status=status)

    assigned_count = assign_authority.objects.filter(AUTHORITY=authority_data, status="assigned").count()
    ongoing_count = assign_authority.objects.filter(AUTHORITY=authority_data, status="ongoing").count()
    completed_count = assign_authority.objects.filter(AUTHORITY=authority_data, status="completed").count()

    return render(
        request,
        "authority/view assigned issues.html",
        {
            "data": a,
            "current_status": status,
            "assigned_count": assigned_count,
            "ongoing_count": ongoing_count,
            "completed_count": completed_count,
        },
    )
def authority_viewfeed(request):
    a=feedback.objects.select_related(
        "ASSIGN__AUTHORITY", "ASSIGN__REQUEST", "USER"
    ).filter(ASSIGN__AUTHORITY__LOGIN=request.user).order_by("-date")
    return render(request,"authority/view feedback.html",{"data":a})


def user_register(request):
     if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        photo=request.FILES.get('photo')
        ward=request.POST['ward']
        place=request.POST['place']
        pin=request.POST['pin']
        post=request.POST['post']

        if User.objects.filter(username=username).exists():
            return _alert("Username already exists", "/myapp/user_register/")
        if photo is None:
            return _alert("Photo is required", "/myapp/user_register/")
        
        group, _ = Group.objects.get_or_create(name="User")
        user=User.objects.create_user(username=username,password=password)
        user.save()
        user.groups.add(group)
        u=user_table()
        u.name=name
        u.phone=phone
        u.email=email
        u.image=photo
        u.ward=ward
        u.place=place
        u.pin=pin
        u.post=post
        u.status='pending'
        u.LOGIN=user
        u.type='user'
        u.save()
        return _alert("Registration submitted successfully. Wait for admin approval.", "/myapp/login_get/")
     return render(request,"user/register.html")
 
def user_sendfeedback(request, id):
    assignment = get_object_or_404(
        assign_authority.objects.select_related("REQUEST", "AUTHORITY"),
        id=id,
        REQUEST__USER__LOGIN=request.user,
    )
    profile = _get_user_profile(request.user)
    if request.method == 'POST':
        feedback_text=request.POST['feedback']
        rating=request.POST['rating']
        feed, _ = feedback.objects.update_or_create(
            ASSIGN=assignment,
            USER=profile,
            defaults={
                "feedback": feedback_text,
                "ratings": rating,
                "date": date.today(),
            },
        )
        return _alert("send sucessfully", "/myapp/user_viewfeedback/")
        
    existing_feedback = feedback.objects.filter(ASSIGN=assignment, USER=profile).first()
    return render(
        request,
        "user/send feedback.html",
        {"data": assignment, "existing_feedback": existing_feedback},
    )
def user_sendreq(request):
     profile = _get_user_profile(request.user)
     if request.method == 'POST':
        title=request.POST['title']
        description=request.POST['description']
        image=request.FILES.get('image')
        if image is None:
            return _alert("Please upload an image", "/myapp/user_sendreq/")
        req=request_table()
        req.USER=profile
        req.title=title
        req.status='pending'
        req.descreption=description
        req.image=image
        req.date=date.today()
        req.save()
        
        return _alert("req send sucessfully", "/myapp/user_requeststat/")
    
    
     return render(request,"user/send req.html")
def user_viewassigned(request,id):
    a=assign_authority.objects.select_related("REQUEST", "AUTHORITY").filter(
        REQUEST_id=id, REQUEST__USER__LOGIN=request.user
    )
    
    return render(request,"user/view assigned.html",{"data":a})
def user_viewfeedback(request):
    a=feedback.objects.select_related(
        "ASSIGN__AUTHORITY", "ASSIGN__REQUEST"
    ).filter(USER__LOGIN=request.user).order_by("-date")
    return render(request,"user/view feedback.html",{"data":a})
def user_requeststat(request):
    
     u=request_table.objects.filter(USER__LOGIN=request.user).order_by("-date")
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
