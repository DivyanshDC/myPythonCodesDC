#
#DO NOT RUN IN PYTHON SHELL
#This program is just for fun. I don't intend to develop much here.
import os
def game():
    import msvcrt
    import time
    from random import randint
    w=True
    n=1
    while w:
        s=10**(n-1)
        e=(10**n)-1
        q=randint(s,e)
        i=5
        while i>0:
            print "Level",n
            print q," "*10,"Seconds remaining:",i
            time.sleep(1)
            while msvcrt.kbhit():
                msvcrt.getwch()
            i-=1
            os.system("cls")
        os.system("cls")
        while True:
            try:
                p = int(raw_input("Please enter the number: "))
                break
            except ValueError:
                print "Oops! That was not a number!"
        if p==q:
            print "Match!"
            n+=1
            print "Proceeding to lvl ", n
            os.system("pause")
            os.system("cls")
        else:
            print "You lost! Resetting, the number was",q
            print "Resetting"
            n=1
            os.system("pause")

a=raw_input("press enter to begin")
if a=="":
    print "And the game begins \n You'll see a number for 5 seconds"
    os.system("pause")
    os.system("cls")
    game()
