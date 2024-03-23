"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
# from django.conf import settings
# from django.conf.urls.static import static
from captcha.urls import urlpatterns as captcha_urls


urlpatterns = [
    path('admin/', admin.site.urls),
   
     
    path('',include('apps.urls')),
    
    path('captcha/', include('captcha.urls')),


]
    # path('contact',include('apps.urls')),
    # path('about',include('apps.urls')),
    # path('services',include('apps.urls')),
    # path('blog',include('apps.urls')),
    # path('Login',include('apps.urls')),
    # path('Logout',include('apps.urls')),
    # path('Signup',include('apps.urls')),
    # # path('account/',include('apps.urls'))
    
# ]+ static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
