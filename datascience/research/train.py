import os
import argparse
from typing import Union
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from raopred.data_preparation import clean_text


vectorizer = TfidfVectorizer(lowercase=False, max_features=50)


def load_json(path_json: str):
    return pd.read_json(path_json, orient='values')


def clean_col(row, col):
    return clean_text(row[col])


def merge_cols(row, col1, col2):
    return row[col1] + ' ' + row[col2]


def get_data(df: pd.DataFrame):
    df['cleaned_title'] = df.apply(lambda x: clean_col(x, 'request_title'), axis =1)
    df['cleaned_text'] = df.apply(lambda x: clean_col(x, 'request_text'), axis =1)
    df['cleaned_all'] = df.apply(lambda x: merge_cols(x, 'cleaned_title', 'cleaned_text'), axis =1)
    df['len_text'] = df['request_text'].str.len()
    return np.array(df[[
        'cleaned_all',
        'len_text',
        'number_of_downvotes_of_request_at_retrieval',
        'number_of_upvotes_of_request_at_retrieval',
        'request_number_of_comments_at_retrieval',
    ]])


def get_labels(df: pd.DataFrame):
    return np.array(df['requester_received_pizza']).astype(int)


def preprocess_data_tfidf(
    X_train: np.array, X_test: np.array, max_features: int) -> Union[
        TfidfVectorizer, np.array, np.array]:
    vectorizer = TfidfVectorizer(stop_words=None,
                            lowercase=False,
                            max_features=max_features)

    features_train = vectorizer.fit_transform(X_train[:,0]).toarray()
    features_test = vectorizer.transform(X_test[:,0]).toarray()

    features_train = np.hstack((features_train, X_train[:,1:]))
    features_test = np.hstack((features_test, X_test[:,1:]))
    return (vectorizer, features_train, features_test)


def evaluate(model: svm, X_test: np.array, y_test: np.array):
    pred = model.predict(X_test)
    print('The test accuracy is: ', accuracy_score(y_test, pred))
    print('Classification report')
    print(classification_report(y_test, pred))
    conf_matrix = confusion_matrix(y_test, pred, normalize='true')
    print(conf_matrix)


def train(model: svm, X_train: np.array, y_train: np.array):
    model.fit(X_train, y_train)
    return model


def get_class_balance(l: np.array):
    percent_1 = np.sum(l)/len(l)
    return {0: percent_1, 1: 1-percent_1}


def save_as_pickle(obj, path: str):
    with open(path, 'wb') as output:
        pickle.dump(obj, output)


def training_pipeline(max_features, kernel, C):
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    df = load_json(os.path.join(root_dir, 'research', 'pizza_data.json'))

    print('Extracting and preparing data for training ...')
    data = get_data(df)
    labels = get_labels(df)

    X_train, X_test, y_train, y_test = train_test_split(data, 
                                                    labels, 
                                                    test_size=0.15, 
                                                    random_state=8)
    vect, X_train, X_test = preprocess_data_tfidf(X_train, X_test, max_features)
    print('Shape training data:', X_train.shape)

    print('Train model ...')
    model = svm.SVC(kernel=kernel, C=C, class_weight=get_class_balance(labels))
    print(model.get_params())
    train(model, X_train, y_train)

    print('Evaluate model...')
    evaluate(model, X_test, y_test)

    print('Save model and vectorizer as pickle...')
    save_as_pickle(model, os.path.join(root_dir, 'raopred/pickles/', 'model.pickle'))
    save_as_pickle(vect, os.path.join(root_dir, 'raopred/pickles/', 'vectorizer.pickle'))


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Training for Random Acts of Pizza prediction')
    parser.add_argument('-mf', '--max-features', default=100, type=int,
                        help='number of words for text vectorization')
    parser.add_argument('-k', '--kernel', default='linear', type=str, help='type of kernel for svm')
    parser.add_argument('-C', default='1.', type=float, help='C value for svm')

    args = parser.parse_args()
    training_pipeline(max_features=args.max_features, kernel=args.kernel, C=args.C)