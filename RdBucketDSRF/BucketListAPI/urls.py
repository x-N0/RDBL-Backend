from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
                  url(r'^bucketlists/$', BucketListCreationView.as_view(), name='Create Bucket'),
                  url(r'^bucketlists/(?P<pk>\d+)/$', BucketListGenView.as_view(), name='Bucket Mod'),
                  url(r'^bucketlists/(?P<pk>\d+)/comments/$', CommentCreationView.as_view(),
                      name='Create Comment'),
                  url(r'^bucketlists/(?P<pk>\d+)/comments/(?P<id>\d+)/$', CommentGenView.as_view(),
                      name='Comment Mod'),
                  url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = format_suffix_patterns(urlpatterns)
