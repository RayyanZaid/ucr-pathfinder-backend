from typing import List
import icalendar
from ScheduleScreen.Course import Course

# William -- Business Layer (Modifying the input data)
# Takes in the .ics file content as a string.
# Rreturns a list of Course objects
def parseICS(fileContent : str) -> List[Course]:
    courseList = []
    calendar = icalendar.Calendar.from_ical(fileContent)
    
    for event in calendar.walk('VEVENT'):
        location = event.get("LOCATION")
        bStart = location.find("Building:") + 10
        bEnd = location.find("Room:") - 1
        rStart = bEnd + 1 + 6
        locationInfo = {
            "buildingName": location[bStart:bEnd],  # Building Name ex. Winston Chung
            "roomNumber": location[rStart:],        # Building Number ex. 1000
            "geoLocation": []
        }

        summary = event.get('SUMMARY').split()
        className = ""
        cEnd = len(summary) - 4
        for x in range(0, cEnd):
            className = className + summary[x] + " "
        className = className + summary[cEnd] # Class Name ex. Introduction to Computer Science
        courseNum = summary[-3] + " " + summary[-2] + " " + summary[-1] # department, number, section, ex. CS 100 01
        
        description = event.get('DESCRIPTION')
        iStart = description.find("Instructor:") + 11
        instructor = description[iStart:] # Professor Name ex. William Huang (Primary)

        timeInfo = {
            "startTime": event.get("DTSTART").dt, # Class Time
            "endTime": event.get("DTEND").dt,     # Class End Time
            "rRule": event.get("RRULE")           # Recurrence Rule ex. which days, repitition frequency, expiration date
        }
        
        courseList.append(Course(className, courseNum, instructor, locationInfo, timeInfo))
    return courseList

# Rayyan -- Persistence Layer (Database Access)
def saveScheduleToFirebase(userID : str , schedule : List[Course]) -> None:

    # Takes in the userID and schedule. Saves the schedule to the user's document in Firebase

    print()




# This is the main function
def inputSchedule(userID : str , file_content : str):

    print(file_content)
    print(userID)
    schedule : List[Course] = parseICS(fileContent=file_content)

    saveScheduleToFirebase(userID=userID, schedule=schedule)

