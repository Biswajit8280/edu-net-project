

# Create your tests here.
from django.test import TestCase

class NotesTestCase(TestCase):
    def setUp(self):
        # Create test data
        role = Role.objects.create(name='Student')
        User.objects.create_user(username='student1', password='password', role=role)

    def test_user_creation(self):
        user = User.objects.get(username='student1')
        self.assertEqual(user.role.name, 'Student')
