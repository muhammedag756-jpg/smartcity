"""
URL configuration for smartcity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [  # path('admin/', admin.site.urls),
    path('index/',views.index),
    path('login_get/',views.login_get),
    path('admin_addauthority/',views.admin_addauthority),
    path('admin_assignauthority/<id>',views.admin_assignauthority),
    path('admin_authorityfeedback/',views.admin_authorityfeedback),
    path('admin_authorityfeedbackwithid/<id>',views.admin_authorityfeedbackwithid),
    path('admin_edit/<id>',views.admin_edit),
    path('delete_authority/<id>',views.delete_authority),
    path('admin_verify/',views.admin_verify),
    path('admin_view_assign/',views.admin_view_assign),
    path('admin_viewauthority/',views.admin_viewauthority),
    path('admin_viewreq/',views.admin_viewreq),
    path('authority_updatestat/<id>',views.authority_updatestat),
    path('authority_markongoing/<id>',views.authority_markongoing),
    path('authority_markcompleted/<id>',views.authority_markcompleted),
    path('authority_viewissues/',views.authority_viewissues),
    path('authority_viewfeed/',views.authority_viewfeed),
    path('user_register/',views.user_register),
    path('user_sendfeedback/<id>',views.user_sendfeedback),
    path('user_sendreq/',views.user_sendreq),
    path('user_viewassigned/<id>',views.user_viewassigned),
    path('user_viewfeedback/',views.user_viewfeedback),
    path('user_requeststat/',views.user_requeststat),
    path('admin_home/',views.admin_home),
    path('authority_home/',views.authority_home),
    path('user_home/',views.user_home),
    path('accept_user/<id>',views.accept_user),
    path('reject_user/<id>',views.reject_user),
    path('block_user/<id>',views.block_user),
    path('unblock_user/<id>',views.unblock_user),
    path('assigned_details/',views.assigned_details),
]
