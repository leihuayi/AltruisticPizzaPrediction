import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


punctuation = list(",.?!(){}[]-_\"'\\;:+*<>@#§^$%&|/") + ['\n', '\r', '\t', '...', '..']
try:
    stop_words = set(stopwords.words('english'))
except Exception as e:
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')

stop_words = set(stopwords.words('english'))
stop_words.add("request")
stop_words.add("edit")


lemmatizer = WordNetLemmatizer()
tag_dict = {"J": wn.ADJ,
            "N": wn.NOUN,
            "V": wn.VERB,
            "R": wn.ADV}


def extract_wnpostag_from_postag(tag):
    #take the first letter of the tag
    #the second parameter is an "optional" in case of missing key in the dictionary 
    return tag_dict.get(tag[0].upper(), None)


def lemmatize_tupla_word_postag(tupla):
    """
    giving a tupla of the form (wordString, posTagString) like ('guitar', 'NN'), return the lemmatized word
    """
    tag = extract_wnpostag_from_postag(tupla[1])
    return lemmatizer.lemmatize(tupla[0], tag) if tag is not None else tupla[0]


def correspondance_miswrite(word: str) -> str:
    if word == "im":
        return "i'm"
    elif word == "ive":
        return "i've"
    else:
        return word


def clean_text(sentence: str) -> str:
    """
    Processes a sentence to keep only important words
    """
    sentence = sentence.lower()
    original_words = word_tokenize(sentence)
    tagged_words = nltk.pos_tag(original_words) #returns a list of tuples: (word, tagString) like ('And', 'CC')
    lemmatized_words = [ lemmatize_tupla_word_postag(ow) for ow in tagged_words ]
    cleaned_words = [ 
        w for w in lemmatized_words if (w not in punctuation) and (w not in stop_words)
    ]
    cleaned_words = [ correspondance_miswrite(w) for w in cleaned_words ]
    return ' '.join(cleaned_words)