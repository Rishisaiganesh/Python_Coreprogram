''' 
@Author : Rishisaiganesh
@Date : 10-11-2021
@Tittle :  Taking input from User and Printing Quadaratic

'''
import math 
def perameters(a,b,c):



    det = b * b - 4 * a * c
    sqrtvalue = math.sqrt(abs(det))

    if det > 0:
        print("real and different")
        root1 = (-b + sqrtvalue)/(2*a)
        root2 = (-b - sqrtvalue)/(2*a)
        print("roots are: ", root1 , root2 )
    elif det == 0:
        print("roots are real and same")
        print("root is", -b /(2*a))
    else:
        print("Please Enter proper values") 
        
while True:
 try:         
   a = int(input("Enter the intergers a*a as like b : "))
   b = int(input("Enter the b element for coefficient : "))
   c = int(input("Enter the C element for constant: "))
   if (a == 0):
     print("Give the proper quadratic values")
   else:
      perameters(a,b,c)
   break
 except ValueError as e:
    print( e)