from playsound import playsound
from time import sleep

print("do you want to listening to naruto war music?")

x = input("enter yes/no:")

if ( x == "yes"):

    print("1....")
    sleep(1)
    print("2....")
    sleep(1)
    print("3......")
    sleep(1)
    while True:
        playsound("naruto-war-music.mp3")
elif (x == "no"):
    exit()

