
''' 
@Author : Rishisaiganesh
@Date : 10-11-2021
@Tittle :  Calculating Windchill whill calculating air speed and temeperater

'''
import math
#speed = s
#temperater = t
#windchill = w
try:
        s = float(input("menction the Speed of the air : "))
        t = float(input("menction the temperater in the air: "))
        w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (math.pow(s,0.16))
        print("The wind chill index is", int(round(w)))
        print("The wind chill is:", int(round(w)))

except Exception as e:
    print(e)