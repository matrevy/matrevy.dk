from django.test import TestCase
from django.urls import reverse


class HomeViewTests(TestCase):
    def setUp(self):
        self.url = reverse('home')

    def test_home_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
