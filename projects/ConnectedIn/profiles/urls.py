from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^profile/(?P<pk>\d+)/$', views.show_profile, name="show_profile"),
    url(r'^profile/(?P<pk>\d+)/invite$', views.invite, name="invite_profile"),
    url(r'^profile/(?P<invite_pk>\d+)/accept', views.invite_accept, name="invite_accept"),
    url(r'^invites$', views.view_invites, name="invites"),
    url(r'^friends$', views.view_friends, name="friends"),
]
