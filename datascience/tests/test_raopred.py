import unittest
from raopred.data_preparation import clean_text
from raopred.prediction import predict


class TestRaopred(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRaopred, self).__init__(*args, **kwargs)
        self.text = "I would like a pizza so much please. I would not know how to thank you if you can forward me a pizza. \
            I'll definitely pay you back my friend. Thanks !! https://myphoto.com"

    def test_clean_text(self):
        """Checks the text preprocessing function"""
        res = "would like pizza much please would know thank forward pizza 'll definitely pay back friend thanks http //myphoto.com"
        self.assertEqual(clean_text(self.text), res)

    def test_predict_wrong_shape_raises(self):
        """Checks that the prediction works properly"""
        with self.assertRaises(ValueError):
            label = predict([self.text])

    def test_predict(self):
        """Checks that the prediction works properly"""
        title = "[Request] I really want some food please"
        len_text = len(self.text)
        number_of_downvotes = 2
        number_of_upvotes = 8
        request_number_of_comments = 4
        input = [title+' '+self.text, len_text, number_of_downvotes, number_of_upvotes, request_number_of_comments]
        label = predict(input)
        self.assertTrue(label)