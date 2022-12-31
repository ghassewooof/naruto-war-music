from playsound import playsound
from time import sleep

print("do you want to listening to naruto war music?")

x = input("enter y/n:")

if ( x == "y"):

    print("1....")
    sleep(1)
    print("2....")
    sleep(1)
    print("3......")
    sleep(1)
    playsound("naruto-war-music.mp3")

elif (x == "n"):
    exit() 