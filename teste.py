import mysql.connector
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="14785gab",
    database="db_jogos"
)

query = "SELECT texto, label FROM an_sentimentos"

data = pd.read_sql(query, connection)

connection.close()

X_train, X_test, y_train, y_test = train_test_split(data['texto'], data['label'], test_size=0.2, random_state=42)

vectorizer = CountVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

