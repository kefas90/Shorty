from django.conf.urls import url
from .views import (
    index,
    goto,
)

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<key>\w{6,10})/$', goto, name='goto'),
]
