from typing import List
from ScheduleScreen.Course import Course



# William -- Business Layer (Modifying the input data)

def parseICS(fileContent : str) -> List[Course]:

    # Takes in the .ics file content as a string.

    # Rreturns a list of Course objects

    print()

    return []


# Rayyan -- Persistence Layer (Database Access)
def saveScheduleToFirebase(userID : str , schedule : List[Course]) -> None:

    # Takes in the userID and schedule. Saves the schedule to the user's document in Firebase

    print()




# This is the main function
def inputSchedule(userID : str , file_content : str):

    print(file_content)
    schedule : List[Course] = parseICS(fileContent=file_content)

    saveScheduleToFirebase(userID=userID, schedule=schedule)

