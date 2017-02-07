from django.conf.urls import url

from hello.views import home

urlpatterns = [
    url(r'^$', home, name='Home'),
]
