from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from memories.models import Place


class PlaceTestCase(TestCase):

    # create user, place and get username and description
    def test_should_return_user_place(self):
        user = create_user("Lika")
        place = create_place(user, "Cafe", "Very nice!")

        self.assertEqual("Lika", user.username)
        self.assertEqual("Very nice!", place.description)

    # create 2 users and 4 places.
    # check request: find places only for user with id 1
    def test_should_return_3(self):
        # user and his places
        user = create_user("Lika")
        create_place(user, "Place1", "Beautiful park1")
        create_place(user, "Place2", "Beautiful park2")
        create_place(user, "Place3", "Beautiful park4")

        # user2 and his places
        user2 = create_user("Another username")
        create_place(user2, "Place4", "It shouldn't count as a place for user with id 1")

        places = user.place_set.all()
        response = self.client.get(reverse('memories:memories'))

        self.assertNotEqual(404, response.status_code)
        self.assertEqual(3, places.count())

    # test home url
    def test_home_url(self):
        response = self.client.get(reverse('memories:home'))
        self.assertEqual(200, response.status_code)


def create_user(name):
    user = User.objects.create(username=name)
    return user


def create_place(user, place_name, description):
    place = Place.objects.create(name=place_name, description=description)
    place.users.add(user)
    return place
