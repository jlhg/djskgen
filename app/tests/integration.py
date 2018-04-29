from django.test import SimpleTestCase
from rest_framework import status
from rest_framework.test import APIClient


class APITestCase(SimpleTestCase):
    client = APIClient()


class TestIndexAPI(APITestCase):
    def test_that_it_responds_with_ok_status(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestSecretKeysViewAPI(APITestCase):
    def test_that_it_responds_with_ok_status(self):
        response = self.client.get('/api/secret_keys/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
