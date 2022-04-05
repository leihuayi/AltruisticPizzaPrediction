import unittest
import requests

class TestApi(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestApi, self).__init__(*args, **kwargs)
        self.url = "http://localhost:5000"

    def test_home(self):
        """Checks that the route / is alive"""
        r = requests.get(self.url)
        self.assertEqual(r.text, "RAOP API")

    def test_upload(self):
        """Checks that the file upload works properly"""
        text = "Please give me a pizza I'm starving I'm a poor student without parents"
        r = requests.post(self.url + "/upload", json={"text": text})
        res = r.json()

        self.assertEqual(len(res.keys()), 1)
        self.assertTrue("label" in res.keys())
        self.assertTrue(isinstance(res["label"], bool))