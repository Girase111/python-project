from time import *       # from = 
import random as r

print(time())   # for time delay
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1 
        except :
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)
if __name__ == '__main__':  
    while True:
        ck = input(" READY TO TEST : yes / no : ")
        if ck == 'yes':
            test =["Pollution is a term which even kids are aware of these days. It has become so common that almost everyone acknowledges the fact that pollution is rising continuously",
            "my name is pratiksha girase", "welcome to my  typing speed calculator project in python"]
            test1 = r.choice(test)
            print("**********typing speed ********")
            print(test1)
            print() ## it breaks line  ##
            print()
            time_1 = time()
            testinput = input("Enter : ")
            time_2 = time()

            print('Speed : ',speed_time(time_1,time_2,testinput),"w/sec")
            print("Error : ",mistake(test1,testinput))

        elif ck == 'no':
            print("THANK YOU")
            break 
        else:
            print("wrong input ")