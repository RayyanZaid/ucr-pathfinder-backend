from firebase import db
from firebase_admin import firestore


def deleteSchedule(uid):
    doc_ref = db.collection("students").document(uid)

    doc = doc_ref.get()

    scheduleDictionary = {}
    if doc.exists:

        docInfo = doc.to_dict()

        scheduleDictionary = docInfo.get("schedule", {})  # Extract schedule data, default to empty dictionary if schedule is not present
        
        if 'schedule' in docInfo:
            # Remove the 'schedule' property from the Firestore document
            doc_ref.update({"schedule": firestore.DELETE_FIELD})
    else:
        print("No doc")

    return scheduleDictionary