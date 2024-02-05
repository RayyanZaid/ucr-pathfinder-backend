from firebase import db

import pytz
from datetime import datetime

def getSchedule(uid):

    uid = "rayyanzaid0401@gmail.com"

    doc_ref = db.collection("students").document(uid)

    doc = doc_ref.get()

    scheduleDictionary = {}
    if doc.exists:

        docInfo = doc.to_dict()

        print(docInfo["schedule"])
        
        scheduleDictionary = docInfo["schedule"]
    
    else:
        print("No doc")

    return scheduleDictionary
    