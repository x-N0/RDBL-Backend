from django.shortcuts import render
from rest_framework import generics, exceptions

from .permissions import Owner, Admin
from .serializer import BucketListSerializer
from .models import BucketList
from rest_framework import permissions


# Create your views here.

class BucketListCreationView(generics.ListCreateAPIView):  # Just available for C.
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    permission_classes = (permissions.IsAuthenticated, Owner, Admin)

    def perform_create(self, serializer):
        # Just save the object
        serializer.save(owner=self.request.user)


class BucketListGenView(generics.RetrieveUpdateDestroyAPIView):  # General View because is available for RUD.
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    lookup_field = 'pk'
    permission_classes = (permissions.IsAuthenticated, Owner, Admin)
