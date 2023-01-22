"""stjoseph URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from It import views

from .views import StudentReg, Studentlist ,Studentdetail , StudentUpdate, StudentDelete 


urlpatterns = [
    path("index",views.index, name = "index1" ),
    path("products",views.products, name = "products1" ),
    path("service",views.service, name = "service1" ),
    path("about",views.about, name = "about1" ),
    path("contact",views.contact, name = "contact1" ),
    # FBV
    # path("studentreg",views.studentreg, name = "studentreg" ),
    #CBV
    
   path('studentreg', StudentReg.as_view(), name = 'studentreg'),
   path('<pk>/studentdetail/', Studentdetail.as_view(), name = 'studentdetail'),
   path('',Studentlist.as_view(), name = 'studentlist'),
   path('<pk>/studentupdate/',StudentUpdate.as_view(),name = 'studentupdate'),
   path('<pk>/studentdelete/', StudentDelete.as_view(), name = 'studentdelete'),

    
]
