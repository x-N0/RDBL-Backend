import os

from rest_framework import serializers
from .models import BucketList


# HERE GOES THE SERIALIZATION OF MODELS

class BucketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BucketList
        fields = '__all__'
        read_only_fields = ('date_created', 'date_modified')

    #def create(self, validated_data):
        #dirName = validated_data['ImgPath'] + validated_data['id']
       #"""if os.path.isfile(dirName):
       #     self.change_and_save(dirName, validated_data)
       # else:
        #    os.mkdir(dirName)
        #    self.change_and_save(dirName, validated_data)"""

    def change_and_save(self, dirName, validated_data):
        validated_data['ImgPath'] = dirName
        return self.save()
"""    def validate_image_type(self):
        self.data['Imga']"""