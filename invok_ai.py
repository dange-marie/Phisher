
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from urllib.parse import urlparse
from ai import extract_url_features
import joblib

def phisher_ai(url):
    matrix = extract_url_features(url)
    model = joblib.load('phisher_model.pkl')
    prediction = model.predict(matrix)
    if prediction[0] == 1:
        return 'Fraud'
    else:
        return 'Legit'
