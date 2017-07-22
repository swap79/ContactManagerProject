from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.contacts, name='contacts'),
    url(r'^ManageContact/(?P<pk>\d+)/$', views.edit_contact, name='edit_contact'),
    url(r'^ManageContact/$', views.create_contact, name='create_contact'),
    url(r'^DeleteContact/(?P<pk>\d+)/$', views.delete_contact, name='delete_contact'),
]