from django.urls import path,include
from . import views

urlpatterns = [
    path('viewall/', views.Viewall,name='viewall'),
    path('add/', views.AddPost,name='add'),
    path('view/', views.ViewMyPost,name='view'),
    path('reg/', views.Registration,name='reg'),
]