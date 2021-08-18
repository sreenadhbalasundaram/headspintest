max_date=input("enter todays Date (dd/mm/yy) : ")#todays Date
d,m,y=max_date.split('/')

d=int(d)
m=int(m)
y=int(y)
date=input("enter the date for evaluation (dd/mm/yy) : ")
dd,mm,yy=date.split('/')
dd=int(dd)
mm=int(mm)
yy=int(yy)
future_date=False
#defining the date 3/05/2021 as todays date
if(dd>=d and mm>=m and yy>=y):
    future_date=True
if(dd==d and mm==m and yy==y):
    future_date=False
#if given a future date
if future_date:
    print("The given date is a future date cannot evaluate")
#if date given is not a future date, evaluating if the date is valid or not
else:
    if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
        mx=31
    elif(mm==4 or mm==6 or mm==11):
        mx=30
    #checking for leap year
    elif(yy%4==0 and (yy%100!=0 or yy%400==0)):
        mx=29
    else:
        mx=28
    if(mm<1 or mm>12):
        print("date is invalid")
    elif(dd<1 or dd>mx):
        print("date is invalid")
    else:
        print("date is valid")
