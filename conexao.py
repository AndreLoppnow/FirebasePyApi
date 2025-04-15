import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


try:
  cred = credentials.Certificate("C:/Users/andre/Desktop/Projetos C#/FirebasePyApi/_firebase-admin-sdk.json.json")
  firebase_admin.initialize_app(cred, {
      'databaseURL': 'https://fir-py-1bb9e-default-rtdb.firebaseio.com/'
  })
  print("Firebase inicializado com sucesso!")
except ValueError as e:
  print(f"Erro ao inicializar o Firebase: {e}")
db = db

