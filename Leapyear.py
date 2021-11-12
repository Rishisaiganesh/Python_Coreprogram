'''
 @Author : Rishi sai ganesh
 @Date : 07-11-2021
 @Time : 1.30pm
 @Title : User Input and check the leapyear
 
 '''
def checkYear(year):
  
 
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))
 

year = int(input("Enter the Year:"))
if(checkYear(year)):
    print("it is a Leap Year")
else:
    print("it is not a Leap Year")