''' 
@Author : Rishisaiganesh
@Date : 10-11-2021
@Tittle :  Taking Input from user and adding with zero


'''
def Adding_With_Zero(list,item):
    elements_value = False

    for k in range(0,item-2):
        for l in range(k+1,item-1):
            for m in range(l+1,item):
                if(list[k]+list[l]+list[m] == 0):
                    print(list[k],list[m],list[m])
                    elements_value = True
    if(elements_value == False):
        print("the elements given are invalid:")
    while True:
        try:
            number = int(input("enter number of elemnts:"))
            list = []
            for k in range(0,number):
                value = int(input("enter the elements:"))
                list.append(value)
                item = len(list)
                Adding_With_Zero(list,item)
                break
        except Exception:
            print("You have an exception")