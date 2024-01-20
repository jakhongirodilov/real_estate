from django.test import TestCase
from .models import CustomUser

class CustomUserTestCase(TestCase):
    def test_user_str(self):
        user = CustomUser.objects.create(username='test_user')
        self.assertEqual(str(user), 'test_user')