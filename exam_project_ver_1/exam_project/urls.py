"""exam_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from testApp import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from testApp.forms import EmailValidationOnForgotPassword

urlpatterns = [
    path('',include('blogApp.urls')),
    path('admin/', admin.site.urls),
    path('sign_view/', views.sign_view),
    path('profile_update/', views.profile_update_view),
    path('profile/', views.profile_view),
    path('home/', views.home_view),
    path('java_exam/', views.java_exam_view),
    path('python_exam/', views.python_exam_view),
    path('sql_exam/', views.sql_exam_view),
    path('register/', views.register_view),
    path('logout/', views.logout_view),
   # path('password_reset_email_validation/', views.password_reset_email_validation_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
                                                                name='password_change_complete'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
                                                                name='password_change'),                                                        
    path('reset_password/', auth_views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword,template_name='registration/password_reset.html'),
                                                                name='reset_password'),                                                           
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_sent.html'), 
                                                                name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_form.html'),
                                                                name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
                                                                name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
