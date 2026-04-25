
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from urllib.parse import urlparse
import joblib

def extract_url_features(url):
    parsed_url = urlparse(url)
    url_len = len(url)
    domainlength = len(parsed_url.netloc)
    pathlength = len(parsed_url.path)
    return [[url_len, domainlength, pathlength]]

df = pd.read_csv('All.csv')

features = ['urlLen', 'domainlength', 'pathLength']
target = 'URL_Type_obf_Type'

df[target] = df[target].apply(lambda x: 1 if x == 'Defacement' else 0)

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
joblib.dump(model, 'model.pkl')
