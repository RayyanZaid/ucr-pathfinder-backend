def parse_ics(file_path):

    calendar : str

    with open(file_path, 'r') as file:
        calendar = file.read()

    
    calendarArray = calendar.split('\n')

    currentLineNumber = 0
    numLines = len(calendarArray)
    while(currentLineNumber < numLines):

        eachLine = calendarArray[currentLineNumber]

        # print(eachLine)

        if(eachLine == "BEGIN:VEVENT"):
            print("YAY")

        currentLineNumber += 1


parse_ics("Fall2023.ics")