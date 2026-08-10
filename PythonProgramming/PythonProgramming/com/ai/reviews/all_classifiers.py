# Machine Learning Models
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
# from xgboost import XGBClassifier
# from lightgbm import LGBMClassifier
from sklearn.neural_network import MLPClassifier  # Artificial Neural Network (ANN)
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Define Vectorization Techniques to Test
vectorizers = {
    "Bag of Words (BoW)": CountVectorizer(max_features=1500),
    "TF-IDF Vectorizer": TfidfVectorizer(max_features=1500)
}

# Define All Target Classifiers
classifiers = {
    "Logistic Regression": LogisticRegression(max_iter=1000, random_state=0),
    "K-NN": KNeighborsClassifier(n_neighbors=5),
    "Random Forest": RandomForestClassifier(random_state=0),
    "Decision Tree": DecisionTreeClassifier(random_state=0),
    "Naive Bayes": MultinomialNB(),
    "SVM (Linear)": SVC(kernel='linear', random_state=0),
    # "XGBoost": XGBClassifier(random_state=0, eval_metric='logloss'),
    # "LightGBM": LGBMClassifier(random_state=0, verbose=-1),
    "ANN Classifier": MLPClassifier(hidden_layer_sizes=(50, 25), max_iter=500, random_state=0)
}