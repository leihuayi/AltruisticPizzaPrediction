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
        text = "I would like a pizza so much please. I would not know how to thank you if you can forward me a pizza. \
            I'll definitely pay you back my friend. Thanks !! https://myphoto.com"
        title = "[Request] I really want some food please"

        r = requests.post(self.url + "/upload", json={
            "text": text,
            "title": title,
            "num_downvotes": 2,
            "num_upvotes": 8,
            "num_comments": 4
        })
        print(r)
        res = r.json()

        self.assertEqual(len(res.keys()), 1)
        self.assertTrue("label" in res.keys())
        self.assertTrue(res["label"])