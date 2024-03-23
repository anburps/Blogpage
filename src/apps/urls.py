from django.urls import path
from apps import views



urlpatterns = [
   path("", views.handlesLogin, name='handlesLogin'),
   path('home', views.home, name='home'),  
   path('contact', views.contact_us, name='contact_us'),  
   path("about", views.about, name='about'), 
   path("services", views.services, name='services'),  
   path("blog", views.blog, name='blog'),  
   
   path('Logout', views.Logout, name='Logout'), 
   path("Signup", views.HandlesSignup, name='HandlesSignup'), 
   path('gallery', views.gallery, name='gallery'),
   path('photo/<str:pk>/', views.viewPhoto, name='photo'),
   path('add/', views.addPhoto, name='add'), 
   
]
