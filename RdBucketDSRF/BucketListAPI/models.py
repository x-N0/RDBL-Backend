from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import filesizeformat
from django.utils.deconstruct import deconstructible
import magic.magic as magic
from django_comments.models import CommentAbstractModel
from django.contrib.contenttypes.models import ContentType


# Create your models here.


class BucketList(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    description= models.CharField(max_length=3000, blank=True, unique=True)
    owner = models.ForeignKey('auth.User', related_name='bucketlists', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    ImgPath = models.ImageField(upload_to="secured/", null=True, blank=True)

    def __str__(self):
        """Return a string representation of the model instance."""
        return "{}".format(self.name)


@deconstructible
class FileValidator(object):
    error_messages = {
        'max_size': ("Ensure this file size is not greater than %(max_size)s."
                     " Your file size is %(size)s."),
        'min_size': ("Ensure this file size is not less than %(min_size)s. "
                     "Your file size is %(size)s."),
        'content_type': "Files of type %(content_type)s are not supported.",
    }

    def __init__(self, max_size='30 MB', min_size=None, content_types=('.jpg', '.png', '.jpeg')):
        self.max_size = max_size
        self.min_size = min_size
        self.content_types = content_types

    def __call__(self, data):
        if self.max_size is not None and data.size > self.max_size:
            params = {
                'max_size': filesizeformat(self.max_size),
                'size': filesizeformat(data.size),
            }
            raise ValidationError(self.error_messages['max_size'],
                                  'max_size', params)

        if self.min_size is not None and data.size < self.min_size:
            params = {
                'min_size': filesizeformat(self.mix_size),
                'size': filesizeformat(data.size)
            }
            raise ValidationError(self.error_messages['min_size'],
                                  'min_size', params)

        if self.content_types:
            content_type = magic.from_buffer(data.read(), mime=True)
            data.seek(0)

            if content_type not in self.content_types:
                params = {'content_type': content_type}
                raise ValidationError(self.error_messages['content_type'],
                                      'content_type', params)

    def __eq__(self, other):
        return (
                isinstance(other, FileValidator) and
                self.max_size == other.max_size and
                self.min_size == other.min_size and
                self.content_types == other.content_types
        )


"""class PhotoBucketList(models.Model):
    Bucket = models.OneToOneField(BucketList, on_delete=models.CASCADE)"""


class CustomComment(CommentAbstractModel):
    bucket= models.ForeignKey(BucketList, related_name='customcomments', verbose_name='Bucket',
                              on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     verbose_name='content type',
                                     related_name="content_type_set_for_%(class)s",
                                     on_delete=models.CASCADE, default=BucketList)
    object_pk = models.PositiveIntegerField('object ID', default=bucket)
    content_object = GenericForeignKey(ct_field="content_type", fk_field="object_pk")
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=1)
    submit_date = models.DateTimeField('date/time submitted', db_index=True, auto_now=True, editable=False)
