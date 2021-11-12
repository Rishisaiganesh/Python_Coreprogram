''' 
@Author : Rishisaiganesh
@Date : 10-11-2021
@Tittle :  Taking Input from user and print 2D array

'''
def array_two(rows_number,columns_number):

    matrix = [] 
    print("Enter the entries row wise:") 
  
    for i in range(rows_number):    
        a =[] 
        for j in range(columns_number):      
            a.append(int(input())) 
        matrix.append(a) 
    print("No of Rows ", rows_number, "and" , columns_number, "No of colums :")
    for i in range(rows_number): 
        for j in range(columns_number): 
            print(matrix[i][j], end = " ") 
        print() 
       
try:
  rows_number = int(input("Enter the number of rows:")) 
  columns_number = int(input("Enter the number of columns:")) 
  array_two(rows_number,columns_number) 
except Exception:
    print("You have an exception")