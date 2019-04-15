import math
import random
import statistics
random.seed(0)
events=[]
completed=[]
queues=[]
#creates arrival event and adds to events
def makeArrivalEvent(maxArrival,avgService):
    arrivalTime='{0:05d}'.format(random.randint(0,maxArrival))
    serviceTime='{0:05d}'.format(random.randint(0,2*avgService))
    events.append(arrivalTime+'A9999999'+serviceTime)

#generates idle time, teller event string, and append to events
def makeTellerEvent(currentTime,tellerNumber):
    idleTime=random.randint(0,60)
    wakeUpTime=(currentTime+idleTime)
    tellerNumber1='{0:02d}'.format(tellerNumber)
    events.append('{0:05d}'.format(wakeUpTime)+'T'+tellerNumber1+'{0:05d}'.format(idleTime)+'99999')

#creates service event string and appends to events
def makeServiceEvent(currentTime,tellerNumber,arrivalTime,serviceTime):
    completionTime=(currentTime+serviceTime)
    waitTime=currentTime-arrivalTime
    events.append('{0:05d}'.format(completionTime)+'S'+'{0:02d}'.format(tellerNumber)+'{0:05d}'.format(waitTime)+'{0:05d}'.format(serviceTime))

#returns character representing type of event
def getType(event):
    return event[5]
#returns time stored in string as int
def getTime(event):
    return int(event[0:5])
#returns teller number as int
def getTeller(event):
    return int(event[6:8])
#returns the wait timeas int
def getWait(event):
    return int(event[8:13])
#returns service time as int
def getService(event):
    return int(event[13:18])

#iterates through event string to determine max wait time and build list of visit times
def analyzeResults():
    maxwait=0
    visittimes=[]
    for i in completed:
        wait = getWait(i)
        maxwait = max(wait,maxwait)
        visittimes.append(wait+getService(i))
    return maxwait,statistics.mean(visittimes),statistics.pstdev(visittimes)



#sets random seed, initializes three module variables, and generates initial events
def initialize(nCustomers,nTellers,maxArrival,avgService,singleQueue,seed):
    random.seed(seed)
    events.clear()
    completed.clear()
    queues.clear()
    if singleQueue==True:
        queues.append([])
    else:
        for i in range(nTellers):
            queues.append([])
    for i in range(nCustomers):
        makeArrivalEvent(maxArrival,avgService)
    print ("number of arrival events", len(events))
    for i in range(nTellers):
        makeTellerEvent(0,i)
    print ("number of teller events", len(events))
    
