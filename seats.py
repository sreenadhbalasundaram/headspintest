seat=int(input("enter seat number:  "))
#checking for seat 
if seat>0 and seat<73:
    if seat%8==1 or seat%8==4:
        print('L')
    elif seat%8==2 or seat%8==5:
        print('M')
    elif seat%8==3 or seat%8==6:
        print('U')
    elif seat%8==7:
        print('SL')
    else:
        print('SU')
else:
    print('invalid seat number')
