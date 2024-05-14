import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="14785gab",
    database="db_jogos"
)

query = "SELECT texto, label FROM an_sentimentos"

data = pd.read_sql(query, connection)

connection.close()