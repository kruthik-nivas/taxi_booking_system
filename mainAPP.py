from taxi import Taxi

def createTaxi(n):
    taxis=[]
    for i in range(1,n+1):
        a=Taxi(i)
        taxis.append(a)
    return taxis

def getFreeTaxis(taxis,pickupTime,dropPoint):
    freeTaxis=[]
    for t in taxis:
        if ((pickupTime >= t.freeTime) and ((ord(t.currentSpot)-ord(dropPoint))<= (pickupTime - t.freeTime))):
            if t.freeTime <= pickupTime:
                freeTaxis.append(t)
    return freeTaxis

def checkEarnings(taxis):
    ftaxi=taxis[0]
    for i in range(1,len(taxis)):
        if taxis[i].totalEarnings < ftaxi.totalEarnings:
            ftaxi = taxis[i]
    return ftaxi


taxis = createTaxi(4)#number of taxis as 4
while True:
    print('Enter 1 -> To book a Taxi')
    print('Enter 2 -> For Details')
    print('Enter 3 -> To Exit')
    choice = int(input('Enter YOur Choice: '))
    if choice == 1:
        customerID = int(input("Enter customer ID: "))
        pickupPoint = input('Enter Your Pickup Point: ')
        dropPoint = input('Enter your Drop Point: ')
        pickupTime = int(input("Enter Pickup Time in 24hrs Format: "))
        if not((65<=ord(pickupPoint)<=70) and (65<=ord(dropPoint)<=70)):
            print('Valid pick up and drop locations are A,B,C,D,E,F.\nYou have entered an invalid option\n\t\t\tExitting Application!')
            print("--"*60)
            break
        else:
            freeTaxis = getFreeTaxis(taxis,pickupTime,dropPoint)
            if len(freeTaxis)==0:
                print('No taxis available for Your mentioned pickup time sorry for the inconvenience')
                print('You will get notified when a taxi is available')
                print('\t\tExitting Application!')
                print('--'*60)
                break
            else:
                ftaxi = checkEarnings(taxis)
                print('Taxi can be allocated')
                print(f"Taxi -> {ftaxi.id} is allocated")
                ftaxi.booked=True
                ftaxi.updateTaxi(pickupPoint,dropPoint,pickupTime,customerID)
                print("--"*60)
    elif choice==2:
        print('Taxi No:\tTotal Earnings:\nBooking Id\tCustomer Id\tFrom\tTo\PickupTime\tDropTime\tAmount')
        for t in taxis:
            print(f"Taxi -> {t.id}\tTotal Earnings: {t.totalEarnings}")
            print()
            t.printDetails()
            print("--"*60)
    elif choice==3:
        print('\t\tThank you Visit again!')
        break
    else:
        print("You have entered a wrong option")
        print("\t\tExitting Application!")
        print('--'*60)
        break