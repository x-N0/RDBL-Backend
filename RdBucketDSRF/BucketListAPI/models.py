from django.db import models


# Create your models here.

class BucketList(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    ImgPath = models.ImageField(upload_to="secured/", null=True, blank=True)

    def __str__(self):
        """Return a string representation of the model instance."""
        return "{}".format(self.name)


"""class PhotoBucketList(models.Model):
    Bucket = models.OneToOneField(BucketList, on_delete=models.CASCADE)"""
