class Taxi:
    def __init__(self,id):
        self.id=id
        self.currentSpot='A'
        self.freeTime=6
        self.totalEarnings=0
        self.booked=False
        self.tripDetails=[]
    
    def updateTaxi(self,pickupPoint,dropPoint,pickupTime,customerID):
        if ord(pickupPoint)>ord(dropPoint):
            distance=ord(pickupPoint)-ord(dropPoint)
        else:
            distance =ord(dropPoint)-ord(pickupPoint)
        aDistance = distance*15
        if aDistance <= 5:
            self.totalEarnings+=100
            tripPrice = 100
        else:
            val = ((aDistance-5)*10)+100
            self.totalEarnings+=val
            tripPrice = val
        self.freeTime = (pickupTime+distance)
        self.currentSpot = dropPoint
        string = f"{customerID}\t{customerID}\t{pickupPoint}\t{dropPoint}\t{tripPrice}"
        self.tripDetails.append(string)
    
    def printDetails(self):
        if len(self.tripDetails)==0:
            print('No Trips Yet')
        else:
            for d in self.tripDetails:
                print(d)