from django.conf.urls import url, include
from . import views


app_name = 'core'
urlpatterns = [
  url(r'^$', views.home, name='home'),
]
