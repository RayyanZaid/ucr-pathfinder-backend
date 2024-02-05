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

        # print(docInfo["schedule"])
        
        scheduleDictionary = docInfo["schedule"]
    
    else:
        print("No doc")


    scheduleDictionary = getCurrentDayClasses(scheduleDictionary)
    return scheduleDictionary


# 0 -- Monday
# 1 -- Tuesday
# 4 -- Friday

numberToDay = {
    0 : "MO",
    1 : "TU",
    2 : "WE",
    3 : "TH",
    4 : "FR", 
}
def getCurrentDayClasses(scheduleDictionary):

    todaysDayNumber = datetime.today().weekday()

    todaysDayName = numberToDay[todaysDayNumber]
    # Display all classes that have BYDAYs on 'todays_day_number'

    i = 0
    while i < len(scheduleDictionary):

        eachCourse = scheduleDictionary[i]
        daysArray = eachCourse['timeInfo']['rRule']['BYDAY']


        # if no days match, delete the course

        isToday : bool = False

        for eachDay in daysArray:
            
            if eachDay == todaysDayName:
                isToday = True
                break
        
        if not isToday:
            scheduleDictionary.pop(i)
        else:
            i += 1
        

    
    return scheduleDictionary

