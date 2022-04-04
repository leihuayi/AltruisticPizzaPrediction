import os
import pickle
from prepare_data import clean_text


pickles_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'pickles')

with open(os.path.join(pickles_dir,'vectorizer.pickle'), 'rb') as data:
    vectorizer = pickle.load(data)

with open(os.path.join(pickles_dir,'model.pickle'), 'rb') as data:
    model = pickle.load(data)


def predict(input_text):
    cleaned_input = [clean_text(input_text)]
    features_input = vectorizer.transform(cleaned_input).toarray()
    res = model.predict(features_input)
    return bool(res[0])

if __name__=="__main__":
    text = "Just started my new job and my paycheck hasn't rolled in yet.\
    I am down to my last dollar now. Would love a pizza in these trying times. I have held strong for 3 months.\n\n\
    I do also intent to pay-it-forward when I can afford it in a couple of months. Much appreciated!\n\n\
    Edit: I failed to mention I am in Toronto! Nearby pizza chains include 241, Dominoes and Pizza Pizza."
    print('Result prediction request:', predict(text))