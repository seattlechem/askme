from rest_framework.test import APITestCase
import json
from django.http import HttpResponse


class ApiTest(APITestCase):
    def test_ask_post_request(self):
        response = self.client.post('/api/v1/ask/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json.loads(response.content), {"answer": "Sorry we have some connection problems. I didn\'t catch your request"})

    def test_audio_post_request(self):
        response = self.client.post('/api/v1/audio/')
        self.assertEquals(response['Content-Type'], 'audio/mp3')
        self.assertNotEqual(len(response['Content-Length']), 0)
        self.assertEquals(response.status_code, 200)
