"""myproject URL Configuration

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
from django.contrib import admin
from django.urls import path, re_path
from app import views as main_views, forms
import django.contrib.auth.views
from django.contrib.auth.views import LoginView, LogoutView
from datetime import datetime
admin.autodiscover()

from submitPR import views as submitPR_views
from viewPR import views as viewPR_views
from submitQuo import views as submitQuo_views
from viewQuo import views as viewQuo_views
from submitPO import views as submitPO_views
from viewPO import views as viewPO_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', main_views.home, name='home'),
    re_path(r'^contact$', main_views.contact, name='contact'),
    re_path(r'^about$', main_views.about, name='about'),
    re_path(r'^login/$', LoginView.as_view(template_name = 'app/login.html'), name='login'),
    re_path(r'^logout$', LogoutView.as_view(template_name = 'app/index.html'), name='logout'),
    re_path(r'^menu$', main_views.menu, name='menu'),
    re_path(r'^submitPRform$', submitPR_views.submitPR, name='submitPR_form'),
    re_path(r'^submitPRconfirmation$', submitPR_views.submitPRconfirmation, name='submitPR_confirmation'),
    re_path(r'^viewPR$', viewPR_views.viewPR, name='viewPR'),
    re_path(r'^viewPRdetails$', viewPR_views.viewPRdetails, name='viewPRdetails'),
    re_path(r'^submitQuoform$', submitQuo_views.submitQuo, name='submitQuo_form'),
    re_path(r'^submitQuoconfirmation$', submitQuo_views.submitQuoconfirmation, name='submitQuo_confirmation'),
    re_path(r'^viewQuo$', viewQuo_views.viewQuo, name='viewQuo'),
    re_path(r'^viewQuodetails$', viewQuo_views.viewQuodetails, name='viewQuodetails'),
    re_path(r'^submitPO$', submitPO_views.submitPO, name='submitPO'),
    re_path(r'^submitPOdetails$', submitPO_views.submitPOdetails, name='submitPOdetails'),
    re_path(r'^submitPOconfirmation$', submitPO_views.submitPOconfirmation, name='submitPOconfirmation'),
    re_path(r'^viewPO$', viewPO_views.viewPO, name='viewPO'),
    re_path(r'^viewPOdetails$', viewPO_views.viewPOdetails, name='viewPOdetails'),
    re_path(r'^arrejectPR$', main_views.arrejectPR, name='arrejectPR'),
    re_path(r'^selectPr$', main_views.selectPr, name='selectPr'),
    re_path(r'^arapprovePR$', main_views.arapprovePR, name='arapprovePR'),
    re_path(r'^arviewPR$', main_views.arviewPR, name='arviewPR'),
    re_path(r'^arviewPR/$', main_views.arviewPR, name='arviewPR'),
    re_path(r'^larviewPR$', main_views.larviewPR, name='larviewPR'),
    re_path(r'^arviewQ$', main_views.arviewQ, name='arviewQ'),
    re_path(r'^larviewQ$', main_views.larviewQ, name='larviewQ'),
    re_path(r'^arapproveQ$', main_views.arapproveQ, name='arapproveQ'),
    re_path(r'^selectQ$', main_views.selectQ, name='selectQ'),
    re_path(r'^arrejectQ$', main_views.arrejectQ, name='arrejectQ'),
]
