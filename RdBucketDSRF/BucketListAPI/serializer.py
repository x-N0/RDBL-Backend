import os

import django_comments
from django_comments.models import Comment
from rest_framework import serializers
from .models import *


# HERE GOES THE SERIALIZATION OF MODELS
class ShortCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = CustomComment
        fields = ('submit_date', 'user_name', 'owner', 'comment', 'is_public')
        read_only_fields = ('submit_date', 'user_name', 'owner', 'comment', 'is_public')


class CustomCommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = CustomComment
        fields = '__all__'
        read_only_fields = ('ip_address', 'submit_date', 'user_name', 'user_email', 'user_url', 'user')


class BucketListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    customcomments = ShortCommentSerializer(many=True, read_only=True)
    """serializers.SlugRelatedField(queryset=CustomComment.objects.all(),
                                                 many=True,
                                                 slug_field='comment'"""

    # )
    # Comments =

    class Meta:
        model = BucketList
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified', 'customcomments', 'owner')

    # def create(self, validated_data):
    # dirName = validated_data['ImgPath'] + validated_data['id']
    # """if os.path.isfile(dirName):
    #     self.change_and_save(dirName, validated_data)
    # else:
    #    os.mkdir(dirName)
    #    self.change_and_save(dirName, validated_data)"""

    def change_and_save(self, dirName, validated_data):
        validated_data['ImgPath'] = dirName
        return self.save()


"""    def validate_image_type(self):
        self.data['Imga']"""
