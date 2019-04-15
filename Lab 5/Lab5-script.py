import Lab5
#runs the full simulation
while True:
    Ncustomers = int(input('Number of customers: '))
    Ntellers = int(input('Number of tellers: '))
    hoursOpen = int(input('Number hours bank open: '))
    hoursOpen = hoursOpen*3600
    averageTime = float(input('Average service time in minutes: '))
    averageTime = averageTime*60
    
    print('Queue for per teller (seed = 0)')
    values = Lab5.runSimulation(Ncustomers,Ntellers,hoursOpen,averageTime,False,0)
    Waitmin = (values[0])//60
    Waitsec = (values[0])%60
    Visit = (values[1])/60
    Dev = (values[2])/60
    print ('{0:<20}'.format('maximum wait time'),'{0} {1}:{2:02}'.format('=',Waitmin,Waitsec))
    print ('{0:<20}'.format('mean visit time'),'=',round(Visit,1),'minutes')
    print ('{0:<20}'.format('stdev visit time'),'=',round(Dev,1),'minutes')

    print('Single queue (seed=0)')
    values = Lab5.runSimulation(Ncustomers,Ntellers,hoursOpen,averageTime,True,0)
    Waitmin = (values[0])//60
    Waitsec = (values[0])%60
    Visit = (values[1])/60
    Dev = (values[2])/60
    print ('{0:<20}'.format('maximum wait time'),'{0} {1}:{2:02}'.format('=',Waitmin,Waitsec))
    print ('{0:<20}'.format('mean visit time'),'=',round(Visit,1),'minutes')
    print ('{0:<20}'.format('stdev visit time'),'=',round(Dev,1), 'minutes')
