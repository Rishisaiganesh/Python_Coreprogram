''''
@Author : Rishisaiganesh
@Date: 09-11-2021
@Description: Taking input from user and Calculating Distance'''
import math
 
def calculateDistance(num1,num2):


    distance = math.sqrt(num1 * num1 + num2 * num2)
    print("the distance is : " ,distance)
while True:
     try:
        num1 = int(input(print("Enter x co-ordinate")))
        num2 = int(input(print("Enter y co-ordinate")))
        calculateDistance(num1,num2)
        break
     except Exception:
        print("You have an Exception ")