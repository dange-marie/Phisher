# Phisher AI - URL Threat Detection

Phisher AI is a machine learning project focused on identifying malicious URLs to enhance web security. It specifically targets "Defacement" attacks using behavioral and structural analysis of web addresses.

## 🚀 Features
* **Feature Extraction:** Automatically parses URLs to analyze domain length, path length, and total string length.
* **Predictive Modeling:** Implements a **Random Forest Classifier** for robust and reliable threat detection.
* **Model Persistence:** The trained model is exported using `joblib` for seamless integration into production environments or security pipelines.

## 🛠️ Technical Stack
* **Language:** Python
* **Machine Learning:** Scikit-Learn
* **Data Processing:** Pandas
* **Deployment:** Joblib (Model Serialization)

## 📊 Methodology
1. **Data Processing:** Categorizes URL types from the dataset (`All.csv`) into binary classifications (Defacement vs. Legitimate).
2. **Feature Engineering:** Extracts key numerical features using `urllib.parse`.
3. **Training:** Utilizes a 100-tree Random Forest ensemble to learn complex patterns in URL structures.
4. **Evaluation:** Provides detailed performance metrics, including Accuracy, Precision, and Recall.

## 💻 Getting Started
1. Install dependencies:
   ```bash
   pip install pandas scikit-learn joblib
   python phisher_ai.py
