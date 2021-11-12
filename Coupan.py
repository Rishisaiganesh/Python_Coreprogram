'''
@Author : Rishisaiganesh
@Date : 11-11-2021
@Tittle :  Taking Input and printing N Distance CoupanNumbers
'''
import random

class Coupannumber():

    def __init__(self,coupan):

        self.choose_number = coupan
    def calculatingNumber(self):
        distinct_number = []
        while len(distinct_number) < self.choose_number:
            randam_num = random.randrange(1,999)
            if randam_num not in distinct_number:
                distinct_number.append(randam_num)
            else:
                pass
            return distinct_number
while True:
    try:
        chooseNumber = int(input("Enter the number coupan you have to generate:"))
        if chooseNumber < 0:
            raise ValueError
            continue
        coupan = Coupannumber(chooseNumber)
        Total_RandomNum = coupan.calculatingNumber()
        print("Total Coupan Numbers:", Total_RandomNum)
        break
    except ValueError:
        print("Invalid input")
    except Exception as e:
        print(e)