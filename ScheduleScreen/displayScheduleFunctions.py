from firebase import db
from datetime import datetime
from copy import deepcopy
def getSchedule(uid):

    uid = uid

    doc_ref = db.collection("students").document(uid)

    doc = doc_ref.get()

    scheduleDictionary = {}
    if doc.exists:

        docInfo = doc.to_dict()

        # print(docInfo["schedule"])
        
        scheduleDictionary = docInfo["schedule"]
    
    else:
        print("No doc")

    
    scheduleDictionaryArray = []

    tempScheduleDictionary = {}
    for i in range(5):
        tempScheduleDictionary = deepcopy(scheduleDictionary)
        tempScheduleDictionary = getCurrentDayClasses(tempScheduleDictionary, i)
        tempScheduleDictionary = orderByTime(tempScheduleDictionary)
        scheduleDictionaryArray.append(tempScheduleDictionary)


    return scheduleDictionaryArray

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
def getCurrentDayClasses(tempScheduleDictionary, dayNumber):



    todaysDayName = numberToDay[dayNumber]
    # Display all classes that have BYDAYs on 'todays_day_number'

    i = 0
    while i < len(tempScheduleDictionary):

        eachCourse = tempScheduleDictionary[i]
        daysArray = eachCourse['timeInfo']['rRule']['BYDAY']


        # if no days match, delete the course

        isToday : bool = False

        for eachDay in daysArray:
            
            if eachDay == todaysDayName:
                isToday = True
                break
        
        if not isToday:
            tempScheduleDictionary.pop(i)
        else:
            i += 1
        

    
    return tempScheduleDictionary


def orderByTime(scheduleDictionary):

    sortedCourses = sorted(scheduleDictionary, key=lambda x: x['timeInfo']['startTime'])

    return sortedCourses
