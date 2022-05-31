"""myprot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpat+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)terns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from maincode.views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', index, name="firstpage"),
    path('admin/adddeatils',adddetails,name="adddeatils"),
    path('contact', contact, name="contact"),
    path('contactapi', createapi, name="contactapi"),
    path('about', myinfo, name="data"),
    path('admin/', adminfirst, name="adminfirst"),
    path('login',lgin,name='logindata'),
    path('logout',logout,name='logout'),
    path('forgot',forgot,name='forgot'),
    path('checkotp',checkotp,name="check"),
    path('admin/addnew',addnew,name="addnew"),
    path('admin/showmyall',showallmydata,name="shwomydata"),
    path('admin/addprojects', addproject, name="addprojects"),
    path('admin/delete/<int:myid>', deletedata, name="deletedata"),
    path('admin/deleteone/<int:myid>',deleteone,name="deleteonedata"),
    path('showallprojects', showallprojects, name="showallprojectsmy")
]
