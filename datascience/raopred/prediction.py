import os
import pickle
import numpy as np
from .data_preparation import clean_text


pickles_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'pickles')
if not os.path.exists(pickles_dir) or len(os.listdir(pickles_dir)) == 0 :
    raise FileNotFoundError('Missing model and vectorizer, please download them')


with open(os.path.join(pickles_dir,'vectorizer.pickle'), 'rb') as data:
    vectorizer = pickle.load(data)


with open(os.path.join(pickles_dir,'model.pickle'), 'rb') as data:
    model = pickle.load(data)


def predict(input):
    cleaned_text = [clean_text(input[0])]
    features_input = vectorizer.transform(cleaned_text).toarray()
    if isinstance(input, list) and len(input)>1:
        features_input = np.hstack((features_input, [input[1:]]))
    res = model.predict(features_input)
    return bool(res[0])