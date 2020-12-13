from django.contrib.auth.models import User
from django.test import TestCase

from memories.models import Place


class PlaceTestCase(TestCase):

    def test_should_return_user_place(self):
        user = create_user("Lika")
        place = create_place(user, "Cafe", "Very nice!")

        self.assertEqual("Lika", user.username)
        self.assertEqual("Very nice!", place.description)

    def test_should_return_3(self):
        user = create_user("Lika")
        user2 = create_user("Another username")

        create_place(user, "Place1", "Beautiful park1")
        create_place(user, "Place2", "Beautiful park2")
        create_place(user, "Place3", "Beautiful park4")

        create_place(user2, "Place4", "It shouldn't count as a place")

        places = user.place_set.all()
        self.assertEqual(3, places.count())


def create_user(name):
    user = User.objects.create(username=name)
    return user


def create_place(user, place_name, description):
    place = Place.objects.create(name=place_name, description=description)
    place.users.add(user)
    return place
