from sys import api_version
from django.test import TestCase

from rest_framework.test import APIRequestFactory

from.models import User, Profile
# Create your tests here.


class TestUserModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username = "user1",
            email = "user1@user1.com",
            password = "user1"
        )

        self.profile = Profile.objects.create(
            user = self.user,
            address = "Kochi"
        )

    def test_user(self):
        self.assertEqual(self.user.username, "user1")
        self.assertEqual(self.user.email, "user1@user1.com")

    def test_profile(self):
        self.assertEqual(self.profile.user.username, self.user.username)
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.address, "Kochi")

class TestProfileViews(TestCase):
    
    def test_user_create(self):
        user = {"username":"user2", "email": "user2@user2.com", "password": "user2"}
        factory = APIRequestFactory()
        request = factory.post('/users/user', data=user, format="json")


    def test_user_list(self):
        factory = APIRequestFactory()
        request = factory.get('/users/user')

    def test_profile_create(self):
        profile = {"user": 2, "address": "Tvm"}
        factory = APIRequestFactory()
        request = factory.post('/users/profile', data=profile, format='json')

    def test_profile_put(self):
        factory = APIRequestFactory()
        request = factory.post('/users/profile/1', {"address": "Trivandrum"}, format='json')

    def test_profile_delete(self):
        factory = APIRequestFactory()
        request = factory.delete('/users/profile/1')

