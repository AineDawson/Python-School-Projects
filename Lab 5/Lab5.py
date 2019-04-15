import random
import statistics
import Lab4
#loops through queues list to find shortest sublist and append arrivalEvent.
def processArrival(arrivalEvent):
    y=0
    for i in range((len(Lab4.queues)-1)):
        if len((Lab4.queues[i]))<len((Lab4.queues[i+1])):
            y=i
        elif len((Lab4.queues[i]))>len((Lab4.queues[i+1])):
            y=i+1
    Lab4.queues[y].append(arrivalEvent)

#determines sublist to use, then either serves or breaks
def processTeller(tellerEvent):
    if len(Lab4.queues) == 1:
        sublist = Lab4.queues[0]
    else:
        k = Lab4.getTeller(tellerEvent)
        sublist = Lab4.queues[k]
    if len(sublist) != 0:
        servicetime = Lab4.getService(sublist[0])
        arrivaltime = Lab4.getTime(sublist[0])
        tellerNumber = Lab4.getTeller(tellerEvent)
        currentTime = Lab4.getTime(tellerEvent)
        Lab4.makeServiceEvent(currentTime, tellerNumber
                              , arrivaltime, servicetime)
        sublist.pop(0)
    else:
        currentTime = Lab4.getTime(tellerEvent)
        tellerNumber = Lab4.getTeller(tellerEvent)
        Lab4.makeTellerEvent(currentTime, tellerNumber)

#process' service event by adding serviceEvent to completed and starts next service
def processService(serviceEvent):
    Lab4.completed.append(serviceEvent)
    processTeller(serviceEvent)

#performs the simuation
def runSimulation(nCustomers, nTellers, maxArrival, avgService,singleQueue, seed):
    Lab4.initialize(nCustomers, nTellers, maxArrival, avgService, singleQueue,seed)
    n = len(Lab4.completed)
    while n < nCustomers:
        Lab4.events.sort()
        event = Lab4.events.pop(0)
        eventype = Lab4.getType(event)
        if eventype =='A':
            processArrival(event)
        elif eventype == 'T':
            processTeller(event)
        elif eventype == 'S':
            processService(event)
        n=len(Lab4.completed)
    return(Lab4.analyzeResults())




