from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics, exceptions
from django_comments.models import Comment
from .permissions import Owner, Admin
from .serializer import BucketListSerializer, CustomCommentSerializer
from .models import BucketList, CustomComment
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


class CommentCreationView(generics.ListCreateAPIView):
    queryset = CustomComment.objects.all()
    serializer_class = CustomCommentSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        bucketListPk = self.kwargs['pk']
        amount = self.request.query_params.get('amt')
        if not isinstance(amount, int) or not amount:
            amount = 5
        queryset = CustomComment.objects.filter(bucket=bucketListPk).order_by('submit_date')
        return get_list_or_404(queryset)

    def perform_create(self, serializer):
        bucketListPk=self.kwargs['pk']
        user=self.request.user
        user_ip=self.request.META['REMOTE_ADDR']
        serializer.save(bucket=bucketListPk, user=user,
                        ip_address=user_ip)


class CommentGenView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomCommentSerializer
    lookup_field = 'id'
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        bucketListPk = self.kwargs['pk']
        queryset = CustomComment.objects.filter(bucket=bucketListPk)
        if not queryset:
            raise Http404()
        return queryset
