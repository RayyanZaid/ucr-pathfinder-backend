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


        # timeInfo = {
        
        # dateEnd
        # dateStart
        # daysOfWeek
        # startTime
        # endTime
        
        # }
        
        self.timeInfo = timeInfo