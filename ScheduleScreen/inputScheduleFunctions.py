from typing import List
import icalendar
from ScheduleScreen.Course import Course



# William -- Business Layer (Modifying the input data)
# Takes in the .ics file content as a string.
# Rreturns a list of Course objects
def parseICS(fileContent : str) -> List[Course]:
    calendar = icalendar.Calendar.from_ical(fileContent)
    for event in calendar.walk('VEVENT'):
        print(event.get("SUMMARY") + "\n")
        print("Start Time and End Time: ")
        print(event.get("DTSTART"))
        print(event.get("DTEND"))
        print()
        print("Times per Week: ")
        print(event.get("RRULE"))
        print()
        print(event.get("LOCATION"))
        print("-------------------------------------------\n")
    return []

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

