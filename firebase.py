import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate('credentials.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()

# print(db)

# doc_ref = db.collection("users").document("rzaid")
# doc_ref.set({"first": "Rayyan", "last": "Zaid", "born": 2003})