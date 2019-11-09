from django.shortcuts import render
from rest_framework import generics
from .serializer import BucketListSerializer
from .models import BucketList


# Create your views here.

class BucketListCreationView(generics.ListCreateAPIView):  # Just available for C.
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer

    def perform_create(self, serializer):
        # Just save the object
        serializer.save()


class BucketListGenView(generics.RetrieveUpdateDestroyAPIView):  # General View because is available for RUD.
    queryset = BucketList.objects.all()
    serializer_class = BucketListSerializer
    lookup_field = 'pk'
