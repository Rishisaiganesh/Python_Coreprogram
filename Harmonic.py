'''
 @Author : Rishi sai ganesh
 @Date : 07-11-2021
 @Time : 1.30pm
 @Title : User Input and check Harmonic Number
 
 '''

def nthHarmonic(N) :
    harmonic = 1.00
 

    for i in range(2, N + 1) :
        harmonic += 1 
 
    return harmonic
     
   
if __name__ == "__main__" :
 
    N = int(input("Enter the number:"))
    print(round(nthHarmonic(N)))