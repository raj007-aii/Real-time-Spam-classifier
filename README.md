# SMS/E-mail Spam Classifier Project
This project is a spam classifier that distinguishes between spam and non-spam (ham) messages. The classifier is implemented in a Jupyter Notebook and can be used in a web application created with Streamlit.

## Folder Structure
This folder contains the Jupyter Notebook (spam_classifier.ipynb) where the spam classifier model is trained and evaluated. It also includes the dataset used for training and testing.

spam-app/: This folder contains the web application built with Streamlit. It allows users to input a text message and classify it as spam or ham using the trained classifier.

## Dependencies
The following dependencies are required to run the spam classifier project:

Python 3.x
Jupyter Notebook
Streamlit
scikit-learn
pandas
numpy
nltk
You can install the necessary dependencies using pip:

```
pip install jupyter notebook
pip install streamlit scikit-learn pandas numpy nltk
```
## Running the Jupyter Notebook
To run the Jupyter Notebook, navigate to the notebook/ directory and execute the following command:
```
jupyter notebook spam_classifier.ipynb
```
This will open the notebook in your web browser, where you can run each cell to train the classifier, evaluate its performance, and save the trained model.

## Running the Web Application
To run the web application, navigate to the spam-app/ directory and execute the following command:
```
streamlit run app.py
```
This will start the Streamlit web server, and you can access the application by opening the provided URL in your web browser. The web application allows you to input a text message and get the predicted class (spam or ham) from the trained classifier.

## Resources
spam_classifier.ipynb: Jupyter Notebook containing the code for training the spam classifier.

spam.csv: Dataset used for training and testing the classifier.

spam-app/app.py: Streamlit web application code for using the trained classifier.

spam-app/requirements.txt: File listing the dependencies required for the web application.

## Acknowledgments
This project is based on machine learning techniques and scikit-learn library. The dataset used for training the classifier is obtained from kaggle.com
