#for using command line arguments
import sys
if len(sys.argv)==2:
#the value or number in the [1] index of command line gives the range upto which armstrong number is to be calculated
    upper=int(sys.argv[1])

#to find all armstrong numbers less than the given number
for num in range(upper):
   # initialize sum
   sum = 0

   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
   #result
   if num == sum:
       print(num)
