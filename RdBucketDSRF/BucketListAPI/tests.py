from django.test import TestCase
from django.urls import reverse

from .models import BucketList
from rest_framework.test import APIClient
from rest_framework import status


# Create your tests here.

class BucketListModelTest(TestCase):
    def setUp(self):
        # Makes a Model Object to test.
        self.bucket_name = "Develop some TDD"
        self.bucket = BucketList(name=self.bucket_name)

    def test_model_can_create_a_BucketList(self):
        # Test the BucketList Model can create a bucket.
        empty_count = BucketList.objects.count()
        self.bucket.save()
        first_count = BucketList.objects.count()
        self.assertNotEqual(empty_count, first_count)


class BucketListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.bucket_data = {'name': 'Go to Puerto del Cabo'}
        self.response = self.client.post(reverse('Create Bucket'), self.bucket_data, format='json')

    def test_api_BucketList_creation(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self):
        bucketitem = BucketList.objects.get()
        response = self.client.get(
            reverse('Bucket Mod',
                    kwargs={'pk': bucketitem.id}), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketitem)

    def test_api_can_update_bucketlist(self):
        change_bucketlist = {'name': 'Something new'}
        bucket = BucketList.objects.get()
        response = self.client.put(
            reverse('Bucket Mod', kwargs={'pk': bucket.id}),
            change_bucketlist, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        bucketitem = BucketList.objects.get()
        response = self.client.delete(
            reverse('Bucket Mod', kwargs={'pk': bucketitem.id}),
            format='json', follow=True)
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
