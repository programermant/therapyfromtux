import os
import time

def main():
    print("this is free software! edit it and distribute as much as you like(^_^)")
    print("how many times do you want tux to give a inspirational qoute")
    wisesays = int(input("$~"))
    other(wisesays)
    pass

def other(wisesays):
    for i in range(wisesays):
        os.system("fortune | cowsay -f tux")
        amnt = 0
        time.sleep(4)
        amnt + 1
        print(amnt)
        pass

    print("is that enough wisdom or do you want more")
    yesornah = input("")
    if "n" in yesornah:
        main()
    elif "y" in yesornah:
        print("exiting")
        pass

main()
