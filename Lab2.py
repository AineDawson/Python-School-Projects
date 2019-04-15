#takes percentage grade and returns letter grade
def letterGrade(percentage):
    p=round(percentage)
    if 100>=p>=94:
        return ('A')
    elif 93>=p>=90:
        return ('A-')
    elif 89>=p>=87:
        return ('B+')
    elif 86>=p>=83:
        return ('B')
    elif 82>=p>=80:
        return ('B-')
    elif 79>=p>=77:
        return ('C+')
    elif 76>=p>=73:
        return ('C')
    elif 72>=p>=70:
        return ('C-')
    elif 69>=p>=67:
        return ('D+')
    elif 66>=p>=60:
        return ('D')
    else:
        return ('E')


#Calculates wages for employees, including overtime.
def payroll(age,hours,rate):
    pay=0
    if 40>=hours:
        pay=hours*rate
    else:
        pay=(40*rate)+(hours-40)*(rate*1.5)
    pay=round(pay, 2)
    udues=0
    if pay>200:
        if age<60:
            udues=udues+15
        else:
            udues=udues+5
    netpay=pay-udues
    netpay=round(netpay, 2)
    return pay,udues,netpay

#Finds the days in a month for certain years, inluding leap years
def daysInMonth(year,month):
    if month==1:
        return 31
    elif month==3:
        return 31
    elif month==5:
        return 31
    elif month==7:
        return 31
    elif month==8:
        return 31
    elif month==10:
        return 31
    elif month==12:
        return 31
    elif month==4:
        return 30
    elif month==6:
        return 30
    elif month==9:
        return 30
    elif month==11:
        return 30
    else:
        if year%4==0:
            if year%100==0:
                if year%400==0:
                    return 29
                else:
                    return 28
            else:
                return 29
        else:
            return 28


#Determines if two rectangles overlap by comparing the upper left corners and
#side lengths
def rectanglesOverlap(left1,top1,width1,height1,left2,top2,width2,height2):
    if left1>=left2 and height1>=height2 and(abs(left1-left2))<=(width1) and (abs(top1-top2))<=(height1):
        return True
    elif left2>=left1 and height2>=height1 and(abs(left1-left2))<=(width2) and (abs(top1-top2))<=(height2):
        return True
    else: return False
        
