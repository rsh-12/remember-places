from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from memories.models import Place


class PlaceTestCase(TestCase):

    fixtures = ['memories/fixtures/places.json', 'memories/fixtures/users.json']

    def test_should_return_user_place(self):
        user = User.objects.get(pk=2)
        place = Place.objects.get(pk=5)
        self.assertEqual(place.name, 'Большакова')

        self.assertEqual(user.username, 'user1')
        self.assertTrue(place.description.__contains__('улица'))

    def test_should_return_0(self):
        user = User.objects.get(pk=3)
        places = user.place_set.all()
        response = self.client.get(reverse('memories:memories'))

        self.assertNotEqual(404, response.status_code)
        self.assertEqual(2, places.count())

    def test_should_return_3(self):
        user = User.objects.get(pk=2)
        places = user.place_set.count()

        self.assertEqual(places, 2)

    def test_should_return_ok(self):
        user = User.objects.get(pk=3)
        Place.objects.create(name="New place", description="New description", user_id=user.id)
        Place.objects.create(name="New place2", description="New description2", user_id=user.id)

        self.assertEqual(user.place_set.count(), 4)
        self.assertTrue(user.place_set.get(pk=8).name, "Исток")

    def test_home_url(self):
        response = self.client.get(reverse('memories:home'))
        self.assertEqual(200, response.status_code)
