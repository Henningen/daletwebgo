from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wavsearch, name='wavsearch'),
]
