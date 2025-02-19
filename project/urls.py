"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('aditi/',views.aditi),
   # path('alldata/',views.alldata),
    # path('filterdata',views.aditi),
    # path('values',views.aditi),
    # path('valueslist',views.aditi),
    # path('exclude',views.aditi),
    # path('get',views.aditi),
    # path('first/',views.firstdata),
     path('last/',views.lastdata),
    # path('order_by/',views.order),
     path('order_by/',views.all)
]