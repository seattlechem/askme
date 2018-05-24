from rest_framework.test import APITestCase
import json


class ApiTest(APITestCase):
    def test_ask_post_request(self):
        response = self.client.post('/api/v1/ask/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(json.loads(response.content), {"answer": "Sorry we have some connection problems. I didn\'t catch your request"})

    def test_audio_post_request(self):
        import pdb; pdb.set_trace()
        response = self.client.post('/api/v1/audio/')
        self.assertEquals(response.status_code, 302)
