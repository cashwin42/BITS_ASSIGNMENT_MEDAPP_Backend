"""healthappBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from healthappdata.views import MedstList,MedsDetail,TransactionList,TransactionDetail,OrderList,OrderDetail,CartNumberList,CartNumberDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('meds/', MedstList.as_view()),
    path('meds/<int:pk>', MedsDetail.as_view()),
    path('transaction/', TransactionList.as_view()),
    path('transaction/<int:pk>', TransactionDetail.as_view()),
    path('order/', OrderList.as_view()),
    path('order/<int:pk>', OrderDetail.as_view()),
    path('cart/',CartNumberList.as_view()),
    path('cart/<int:pk>',CartNumberDetail.as_view()),
]
