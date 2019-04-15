import math
#Finds largest square number n is divisible by
def maxSquareFactor(n):
    x=0
    for i in range(1,n+1):
        if n%i==0 and (round(math.sqrt(i))**2)==i:
            x=i
    return x

#isbn number check
def checkSymbol(isbn):
    check=0
    for i in range(9):
        a=isbn-(isbn//10)*10
        isbn=(isbn//10)
        b=a*(9-i)
        check=check+b
    tot=check%11
    if tot==10:
        return ('X')
    else:
        return(str(tot))
 
#adds two integers without carrying
def carrylessAdd(x,y):
    a=str(x)
    b=str(y)
    final=0
    if len(a)>len(b):
        z=len(a)
    else:
        z=len(b)
    xchange=x
    ychange=y
    for i in range(z):
        x1=xchange//10
        x2=xchange-(x1*10)
        xchange=x1
        y1=ychange//10
        y2=ychange-(y1*10)
        ychange=y1
        t1=x2+y2
        t2=t1//10
        tt=t1-(t2*10)
        final=final+tt*10**i
    return final

#printing N with minus signs and asterisks.
def printN(n):
    for line in range(1,n+1):
        if n==1:
            print('*')
        elif line==1 or line==n:
            print ('*'+(n-2)*'-'+'*')
        else:
            print ('*'+(line-2)*'-'+'*'+(n-(line+1))*'-'+'*')
