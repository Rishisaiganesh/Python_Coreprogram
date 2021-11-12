'''
 @Author : Rishi sai ganesh
 @Date : 07-11-2021
 @Time : 1.30pm
 @Title : User Input and Replace String Template
 
 '''
name = True

while(name == True):
    # Exception Try
    try:
        Name=input("Enter User Name : ")
        if Name.isalpha(): 
            if len(Name) >= 3:  
                print("Hello", Name, "How are you?")
                flag = False
            else:
                print("Please enter min 3 charators")
                flag = True
        else:
            print("Invalid input ")
            flag = True

    # Exception Catch
    except Exception as e:
        print(e)
        name = True