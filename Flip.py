''' 
@Author : Rishisaiganesh
@Date : 2021-11-09
@Last Modify by : Rishisaiganesh
@Title : find head and tail percentage by using random() function
'''
import random
result = ("HEAD","TAIL")
if_ITnot_Head = 0
if_Itnot_Tail = 0
i = 0
value = True

while (value == True):
    try:
        print("Enter the number of times you want to flip the coin :")
        num = int(input())
        if num>0:
            while(i<=num):
                outcome = random.choice(result)
                if(outcome == "HEAD"):
                    if_ITnot_Head = if_ITnot_Head + 1
                elif (outcome == "TAIL"):
                    if_Itnot_Tail = if_Itnot_Tail + 14
                i = i+1

        percentageTail = str((if_Itnot_Tail/num) * 100)
        percentageHead = str((if_ITnot_Head/num) * 100)

        print("Head :"+percentageHead,"VS Tail:"+percentageTail)

        if percentageHead > percentageTail:
            print("Head Wins with percent : "+percentageHead)
            result = False
        elif percentageHead == percentageTail:
            print("Both Percentages are equal")
            result = True
        else:
            print("Tail Wins with percent : "+percentageTail)
            result = False

    except Exception as e:
        print(e)
        result = True