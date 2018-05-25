"""Test cases for askme."""
from django.test import TestCase


class RouteTests(TestCase):
    """Route test cases."""

    def test_200_status_on_landing(self):
        """Home page test case."""
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_200_status_on_aboutus(self):
        """About us page test case."""
        response = self.client.get('/aboutus')
        self.assertEqual(response.status_code, 200)

    def test_200_status_on_audio(self):
        """Audio route test."""
        response = self.client.get('/audio')
        self.assertEqual(response.status_code, 200)

    def test_save_view(self):
        response = self.client.post('/audio')
        self.assertEquals(response['Content-Type'], 'audio/mp3')
        self.assertNotEqual(len(response['Content-Length']), 0)
        self.assertRaises(KeyError, response)
