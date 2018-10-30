class User:
    def __init__(self):
        self.preferences = []
        self.safeRoutes = False
        self.greenRoutes = False
        self.roadConditions = False
        self.start = None
        self.end = None

    def getPreferences(self):
        # take user input.
        self.safeRoutes = int(input("Enter 1/0 for safe"))
        self.greenRoutes = int(input("Enter 1/0 for green"))
        self.roadConditions = int(input("enter 1/0 for road condition detection"))
        self.preferences = [self.safeRoutes,self.greenRoutes,self.roadConditions]
        return self.preferences

    def setLocation(self,start,end):
        self.start = start
        self.end = end
        ## here self.start and self.end will contain the geo-coded locations (lat-longs of source and destination)


class Algorithms:
    def __init__(self):
        self.routing_algorithm = "using the pyroute2 library as the basis" # to show that we are using the pyroute2 library.
        self.points =[1,2,3,4,5,6,7,8,9,10]  ## for simplicity.
    def main_algorithm(self,unsafePoints,flag):
        if flag ==1 :  ## safety
            return set(self.points)-set(unsafePoints) ## return set of points that are not dangerous
        if flag == 2: ## green routes
            return set(self.points) ## for simplicity
        if flag == 3:
            return set(self.points) ### for simplicity.

    def safeRoutes(self,toLocation,fromLocation):
        print(" getting the safe routes")
        # scrape LA Crime Data
        # clean and preprocess the data
        # build a random forest model and get the features
        # set of dangerous points on the way.
        # make a call to the main algorithm so that it filters off these points and returns a good route.
        unSafePoints = [1,2,3,6]
        safePoints = self.main_algorithm(unSafePoints,1)
        return safePoints

    def greenRoutes(self,toLocation,fromLocation):

        print("getting green routes")
        # Get google image data set
        # Use OpenCV to segment green locations
        # get green locations
        # make a call to the main algorithms so that it returns a PATH with these points.
        greenPoints = [2,3,4] ## for simplicity
        greenPoints = self.main_algorithm(greenPoints,2)
        return greenPoints

    def roadCondition(self,toLocation,fromLocation):
        print("getting road condition information")
        # Scrape live tweets, and complaints from ichangemycity
        # NLP with IBM Watson for sentiment analysis
        # analyse the severity. build a model.
        badRoads = [1,5,6] ## for simplicity
        goodRoad = self.main_algorithm(badRoads,3)
        return goodRoad


class API():
    def __init__(self):
        self.user = User()  ## user can use the API.
        print("getting the pref")
        self.preferences = self.user.getPreferences()
        self.user.setLocation("Malleshwaram","Rajajinagar")
    def getPreferences(self):
        algorithm= Algorithms()
        points = algorithm.points  ### initially, let the points be the route pointed to by pyroutelib2.
        if self.preferences[0] == 1: # safe routes
            points = algorithm.safeRoutes(self.user.start,self.user.end)
        if self.preferences[1] == 1:  ## green routes
            points = algorithm.greenRoutes(self.user.start,self.user.end)
        if self.preferences[2] == 1: ## road conditions
            points = algorithm.roadCondition(self.user.start,self.user.end)
        return points


if __name__ == '__main__':
    api = API()
    points= api.getPreferences()
    print("required path is",points)
