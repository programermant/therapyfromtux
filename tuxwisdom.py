import os
import time

def main():
    print("how many times do you want tux to give a inspirational qoute")
    wisesays = int(input("$~"))
    other(wisesays)

def other(wisesays):
    for i in range(wisesays):
        os.system("fortune | cowsay -f tux")
        amnt = 0
        time.sleep(4)
        amnt + 1
        print(amnt)

    print("is that enough widom or do you want more")
    yesornah = input("")
    if "n" in yesornah:
        main()
    elif "y" in yesornah:
        print("exiting")

main()
