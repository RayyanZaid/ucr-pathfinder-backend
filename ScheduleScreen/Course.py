class Course:

    def __init__(self, className : str, courseNumber : str, teacherName : str, locationInfo : dict, timeInfo : dict) -> None:
        
        self.className = className
        self.courseNumber = courseNumber
        self.teacherName = teacherName




        # locationInfo = {
        
        #  buildingName : "",
        #  roomNumber : "",
        #  geoLocation : [],
        
        # }


        self.locationInfo = locationInfo

        # I'm keeping them in datetime because I'm not sure how you want them
        
        # You can use strftime() to change datetime to string there are many formats ex strftime("%H:%M") returns string of hour and min
        
        # rRule = recurrence rule
        # What happens when you print rRule vRecur({'FREQ': ['WEEKLY'], 'UNTIL': [datetime.datetime(2024, 3, 15, 22, 59)], 'BYDAY': ['MO', 'WE', 'FR']})
        # I'm just going to leave it as rRule so you can do whatever you want with it, there should be documentation to help you manipulate it
        
        # timeInfo = {
        #   timeStart : datetime,
        #   timeEnd : datetime,
        #   rRule : some type of object
        
        # }
        
        self.timeInfo = timeInfo



    def returnDictionaryForFirebase(self) -> dict:


        courseDictionary = {
            "className" : self.className,
            "courseNumber" : self.courseNumber,
            "teacherName" : self.teacherName,
            "locationInfo" : self.locationInfo,
            "timeInfo" : self.timeInfo
        }

        return courseDictionary