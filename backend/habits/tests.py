from rest_framework.test import APITestCase
from rest_framework import status
from .models import Habit
from django.contrib.auth.models import User


# Create your tests here.

class HabitTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.other_user = User.objects.create_user(username='otheruser', password='othertesspassword')
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        response = self.client.post('/api/habits/', {
            'title': 'Title1',
            'desc': '',
            'start_date': '2026-01-01',
            'type': 'good'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_request(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('/api/habits/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_cannot_see_other_users_habits(self):
        Habit.objects.create(owner=self.other_user, title='Other users habit', start_date='2026-01-01', type='good')
        response = self.client.get('/api/habits/')
        self.assertEqual(len(response.data), 0)


class HabitLogTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(owner=self.user, title='Habit Title', start_date='2026-01-01', type='good')

    def test_log_habit(self):
        response = self.client.post(f'/api/habits/{self.habit.id}/log/', {
            'log_date': '2026-01-01'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cannot_log_bad_habit(self):
        bad_habit = Habit.objects.create(owner=self.user, title='Smoking', start_date='2026-01-01', type='bad')
        response = self.client.post(f'/api/habits/{bad_habit.id}/log/', {
            'log_date': '2026-01-01'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_log_same_day_twice(self):
        self.client.post(f'/api/habits/{self.habit.id}/log/', {'log_date': '2026-01-01'})
        response = self.client.post(f'/api/habits/{self.habit.id}/log/', {'log_date': '2026-01-01'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_log_other_users_habit(self):
        other_user = User.objects.create_user(username='otheruser', password='testpass123')
        other_habit = Habit.objects.create(owner=other_user, title='Other', start_date='2026-01-01', type='good')
        response = self.client.post(f'/api/habits/{other_habit.id}/log/', {'log_date': '2026-01-01'})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)