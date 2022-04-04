import os
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from raopred.prepare_data import clean_text


vectorizer = TfidfVectorizer(lowercase=False, max_features=50)


def load_json(path_json):
    return pd.read_json(path_json, orient='values')


def clean_col(row, col):
    return clean_text(row[col])


def get_data(df):
    return df.apply(lambda x: clean_col(x, 'request_text'), axis =1)


def get_labels(df):
    return np.array(df['requester_received_pizza']).astype(int)


def preprocess_data_tfidf(X_train, X_test):
    vectorizer = TfidfVectorizer(stop_words=None,
                            lowercase=False,
                            max_df=1.,
                            min_df=10,
                            max_features=200,
                            norm='l2',
                            sublinear_tf=True)
                            
    features_train = vectorizer.fit_transform(X_train).toarray()
    features_test = vectorizer.transform(X_test).toarray()
    return (vectorizer, features_train, features_test)


def evaluate(model, X_test, y_test):
    pred = model.predict(X_test)
    print('The test accuracy is: ', accuracy_score(y_test, pred))
    print('Classification report')
    print(classification_report(y_test, pred))
    conf_matrix = confusion_matrix(y_test, pred, normalize='true')
    print(conf_matrix)


def train(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model


def save_as_pickle(obj, path):
    with open(path, 'wb') as output:
        pickle.dump(obj, output)


def training_pipeline():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = load_json(os.path.join(root_dir, 'research', 'pizza_data.json'))

    print('Extracting and preparing data for training ...')
    data = get_data(df)
    labels = get_labels(df)

    X_train, X_test, y_train, y_test = train_test_split(data, 
                                                    labels, 
                                                    test_size=0.15, 
                                                    random_state=8)
    vect, X_train, X_test = preprocess_data_tfidf(X_train, X_test)

    print('Train model ...')
    model = svm.SVC(kernel='linear')
    train(model, X_train, y_train)

    print('Evaluate model...')
    evaluate(model, X_test, y_test)

    print('Save model and vectorizer as pickle...')
    save_as_pickle(model, os.path.join(root_dir, 'raopred/pickles/', 'model.pickle'))
    save_as_pickle(vect, os.path.join(root_dir, 'raopred/pickles/', 'vectorizer.pickle'))


if __name__=="__main__":
    training_pipeline()