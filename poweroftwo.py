'''
 @Author : Rishi sai ganesh
 @Date : 08-11-2021
 @Time : 6pm
 @Title : User input and checking power of 2
 
 '''
n = int(input("Enter the Number:"))
def highestPowerof2(n):
 
    res = 0
    for i in range(n, 0, -1):
         
        # If i is a power of 2
        if ((i & (i - 1)) == 0):
         
            res = i
            break
         
    return res          
print(highestPowerof2(n))