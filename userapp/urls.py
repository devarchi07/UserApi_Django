from django.contrib import admin
from django.urls import path,include
from userapp import views

urlpatterns = [
    path('view-user/',views.viewuser, name='userlist'),
    path('view-seller/',views.viewseller, name='sellerlist'),
    path('add-user/',views.adduser, name='adduser'),
    path('add-seller/',views.addseller, name='addseller'),
    path('del-seller/<int:pk>',views.delseller, name='delseller'),
    path('del-user/<int:pk>/',views.deluser, name='deluser'),
      
]
