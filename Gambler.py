''' 
@Author : Rishisaiganesh
@Date : 11-11-2021
@Tittle :  Gambler Taking input form and checking Percentage of Wins and Loss
'''
import random
class Gambler:                                       

 def __init__(self,Stake,Goal,number):              
        self.Stake = Stake
        self.Goal = Goal
        self.number = number

 def gambler(self,Stake,Goal,number):              

    wincount = 0
    losscount = 0
    counter = 0


    while (Stake > 0 and Stake < Goal and counter < number):   
        try:
           
           counter = counter + 1
           random_generated = random.randint(0,1)    
                                                    
           if (random_generated == 1):
               wincount = wincount + 1
               self.Stake = self.Stake + 1
           else:
               losscount = losscount + 1
               self.Stake = self.Stake - 1
        except ValueError:
                print("You have an exception" )                     

    percent_win = (wincount/number)*100
    percent_loss = 100-percent_win
    print("Number of wins",wincount)
    print("Number of loss",losscount)
    print("win's percentage :",percent_win)
    print("loss's percentage :",percent_loss )
    print("Number of bets",counter)

if __name__ == '__main__':                                
    Stake = int(input("Enter the stake amount :"))
    Goal = int(input("Enter the Goal amount : "))
    number = int(input("Enter number of Bets :"))

    obj = Gambler(Stake,Goal,number)                       
    obj.gambler(Stake,Goal,number)                         

        