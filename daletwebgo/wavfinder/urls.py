from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.wavsearch, name='wavsearch'),
    url(r'^search/$', views.wavsearchredir, name='wavsearchredir'),
    url(r'^search/(?P<search>[^/]+)/$', views.wavsearch, name='wavsearch'),
    url(r'^jobstatus/$', views.jobstatus, name='jobstatus'),
    url(r'^jobstatus/(?P<status>(progress|failed|finished|all))/$', views.jobstatus, name='jobstatus'),
]
