from django.conf.urls import url
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = {
    url(r'^bucketlists/$', BucketListCreationView.as_view(), name='Create Bucket'),
    url(r'^bucketlists/(?P<pk>\d+)/$', BucketListGenView.as_view(), name='Bucket Mod')
}
urlpatterns = format_suffix_patterns(urlpatterns)
