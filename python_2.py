# Have the function PrimeTime(num) take the num parameter being passed and return the string true if the parameter is
# a prime n as mumber, otherwise return the string false. The range will be between 1 and 2^16.
import math as m
def primetim(num):
    if num <2:
        return True
    else:
        print('false')
    for i in range(2,int(m.sqrt(num))):
        if num%i == 0:
            return False
        else :
            return True
print(primetim(int(input())))

