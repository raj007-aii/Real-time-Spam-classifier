import streamlit as st
import pickle

import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
nltk.download('punkt')
nltk.download('stopwords')

def transform_text(text):
    # convert all characters to lowercase
    text = text.lower()
    
    # tokenize the text into individual words
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    # remove stopwords and punctuation from the list of words
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    # reduce each word to its root form using stemming
    text = y[:]
    y.clear()

    ps = PorterStemmer()
    for i in text:
        y.append(ps.stem(i))

    # join the list of stemmed words back into a single string
    y = ' '.join(y)
    
    return y


# Load the saved vectorizer and model objects from disk using pickle.
tfidf = pickle.load(open('vectroizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Predict'):

    # preprocess the input message using transform_text function defined above.
    transform_sms = transform_text(input_sms)

    # vectorize the preprocessed message using tfidf object loaded from disk.
    vector_input = tfidf.transform([transform_sms])

    # predict whether or not the message is spam using model object loaded from disk.
    result = model.predict(vector_input)[0]

    # display result based on predicted value.
    if result == 1:
        st.header('Spam')
    else:
        st.header("Not Spam")


