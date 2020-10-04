#from . import views
from django.urls import path, re_path
from django.conf.urls import  url
from django.views.generic import TemplateView

urlpatterns = [
    url('', TemplateView.as_view(template_name='about.html')),]
