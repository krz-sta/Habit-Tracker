from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

# Create your tests here.

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

class RegisterTests(APITestCase):

    def test_register(self):
        response = self.client.post('/api/users/register/', {
            'username': 'newuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_duplicate_username(self):
        User.objects.create_user(username='existinguser', password='testpass123')
        response = self.client.post('/api/users/register/', {
            'username': 'existinguser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_me_authenticated(self):
        user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=user)
        response = self.client.get('/api/users/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')

    def test_me_unauthenticated(self):
        response = self.client.get('/api/users/me/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)