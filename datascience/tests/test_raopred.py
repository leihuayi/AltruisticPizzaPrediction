import unittest
from raopred.data_preparation import clean_text
from raopred.prediction import predict


class TestRaopred(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRaopred, self).__init__(*args, **kwargs)
        self.text = "Just started my new job and my paycheck hasn't rolled in yet.\
        I am down to my last dollar now. Would love a pizza in these trying times. I have held strong for 3 months.\n\n\
        I do also intent to pay-it-forward when I can afford it in a couple of months. Much appreciated!\n\n\
        Edit: I failed to mention I am in Toronto! Nearby pizza chains include 241, Dominoes and Pizza Pizza."

    def test_clean_text(self):
        """Checks the text preprocessing function"""
        res = "start new job paycheck n't roll yet.i last dollar would love pizza try time hold strong 3 month also intent pay-it-forward \
            afford couple month much appreciate fail mention toronto nearby pizza chain include 241 domino pizza pizza"
        self.assertEqual(clean_text(self.text), res)

    def test_predict(self):
        """Checks that the prediction works properly"""
        label = predict(self.text)
        self.assertTrue(isinstance(label, bool))