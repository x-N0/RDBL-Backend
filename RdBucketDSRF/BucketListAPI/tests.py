from django.test import TestCase
from .models import BucketList


# Create your tests here.

class BucketListModelTest(TestCase):
    """Test suite for a single model"""
    def __init__(self):
        self.modelSet()

    def modelSet(self):
        # Makes a Model Object to test.
        self.bucket_name = "Develop some TDD"
        self.bucket = BucketList(name=self.bucket_name)

    def test_model_can_create_a_bucketlist(self):
        #Test the BucketList Model can create a bucket.
        empty_count = Bucketlist.objects.count()
        self.bucket.save()
        first_count = Bucketlist.objects.count()
        self.assertNotEqual(empty_count, first_count)

