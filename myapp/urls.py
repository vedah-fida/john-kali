from django.conf.urls import include, url
from . import views

app_name = "myapp"

urlpatterns = [
    url(r'^$', views.second_view, name="basic_view"),
    url(r'^products/$', views.index, name='index'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^login/$', views.user_login, name='login_user'),

]
