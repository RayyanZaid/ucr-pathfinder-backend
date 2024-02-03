import firebase_admin
from firebase_admin import credentials, firestore, auth


# Use a service account.
cred = credentials.Certificate('credentials.json')

app = firebase_admin.initialize_app(cred)

db = firestore.client()


try:

    user = auth.create_user(
        phone_number='+16265342234'
        
    )


except Exception as e:
    print(e)
# print(db)

# doc_ref = db.collection("users").document("rzaid")
# doc_ref.set({"first": "Rayyan", "last": "Zaid", "born": 2003})