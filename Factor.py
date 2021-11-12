'''
 @Author : Rishi sai ganesh
 @Date : 07-11-2021
 @Time : 10.10pm
 @Title : User Input and primefactorial
 
 '''
import math
value = True

def prime_factors(number):
    while number % 2 == 0:
        print(2,)
        number = number / 2

    for i in range(3, int(math.sqrt(number)) + 1, 2):

        while number % i == 0:
            print(i,)
            number = number / i
    if number > 2:
        print(number)
while(value == True):

    try :
        number = int(input("Enter the number to get its prime factor :"))
        prime_factors(number)
        value = False

    except Exception as e:
        print(e)
        value = True