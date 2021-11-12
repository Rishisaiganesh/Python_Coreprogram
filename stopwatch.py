''' 
@Author : Rishisaiganesh
@Date : 11-11-2021
@Tittle :  Taking Input and printing Simulate StopWatch
'''
import time
class Stopwatch:
    try:
        while True:
            start = int(input("To start press 1:"))
            start_Stopwatch = time.time()
            stop_StopWatch =int(input("press 0 to stop:"))
            stoptime = time.time()
            Elapsed = stoptime - start_Stopwatch
            print("Time Elapsed of stopwatch is :", Elapsed,'sec' )
    except ValueError:
        print("You have an Exception")