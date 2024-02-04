from typing import List
from ScheduleScreen.Course import Course
from datetime import datetime

from firebase import db



# William -- Business Layer (Modifying the input data)

def parseICS(fileContent : str) -> List[Course]:

    # Takes in the .ics file content as a string.

    # Rreturns a list of Course objects

    print()

    return []


# Rayyan -- Persistence Layer (Database Access)
def saveScheduleToFirebase(userID : str , schedule : List[Course]) -> None:

    # Takes in the userID and schedule. Saves the schedule to the user's document in Firebase

    firebaseScheduleField : List[dict] = []
    for eachCourse in schedule:

        dictionaryForEachCourse = eachCourse.returnDictionaryForFirebase()

        firebaseScheduleField.append(dictionaryForEachCourse)


    doc_ref = db.collection("students").document(userID)



    doc_ref.set({"schedule" : firebaseScheduleField})
    print()




# This is the main function
def inputSchedule(userID : str , file_content : str):

    print(file_content)
    print(userID)
    schedule : List[Course] = parseICS(fileContent=file_content)
    

    # BEGIN:VEVENT
    # DTSTAMP:20240122T030350Z
    # DTSTART;TZID=America/Los_Angeles:20230928T200000
    # DTEND;TZID=America/Los_Angeles:20230928T212000
    # SUMMARY:COMPILER DESIGN CS 152 001
    # RRULE:FREQ=WEEKLY;UNTIL=20231208T225900;BYDAY=TU,TH
    # TZID:America/Los_Angeles
    # UID:20240122T030352Z-Ellucian
    # LOCATION:Campus: Riverside Building: Bourns Hall Room: A125 
    # DESCRIPTION:CRN: 26876\nCredit Hours: 4.0\nLevel: Undergraduate\nInstructor: Zhao\, Zhijia (Primary) \n
    # END:VEVENT

    locationInfo = {
        "buildingName" : "Bourns Hall",
        "roomNumber" : "A125",
        "geoLocation" : [1,2]
    }

    timeInfo = {
        "dateStart" : datetime(2023,9,28),
        "dateEnd" : datetime(2023,12,8),
        "daysOfWeek" : ["Tuesday" , "Thursday"],
        "startTime" : "20:00",
        "endTime" : "21:20"
    }
    course : Course = Course("COMPILER DESIGN", "CS 152", "Zhao, Zhijia", locationInfo, timeInfo)

    schedule = [course, course]  
    userID = "rayyanzaid0401@gmail.com" 
    saveScheduleToFirebase(userID=userID, schedule=schedule)

