from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from memories.models import Place


class PlaceTestCase(TestCase):
    fixtures = ['memories/fixtures/users.json', 'memories/fixtures/places.json']

    def test_should_return_user_place(self):
        user = User.objects.get(pk=2)
        place = Place.objects.get(pk=9)
        self.assertEqual(place.name, 'University')

        self.assertEqual(user.username, 'test')
        self.assertTrue(place.description.__contains__('Lorem ipsum dolor'))

    def test_should_return_0(self):
        user = User.objects.get(pk=3)
        places = user.place_set.all()
        response = self.client.get(reverse('memories:memories'))

        self.assertNotEqual(404, response.status_code)
        self.assertEqual(0, places.count())

    def test_should_return_3(self):
        user = User.objects.get(pk=2)
        places = user.place_set.count()

        self.assertEqual(places, 3)

    def test_should_return_ok(self):
        user = User.objects.get(pk=3)
        Place.objects.create(name="New place", description="New description", user_id=user.id)
        Place.objects.create(name="New place2", description="New description2", user_id=user.id)

        self.assertEqual(user.place_set.count(), 2)
        self.assertTrue(user.place_set.get(pk=12).name, "New description")

    def test_home_url(self):
        response = self.client.get(reverse('memories:home'))
        self.assertEqual(200, response.status_code)
