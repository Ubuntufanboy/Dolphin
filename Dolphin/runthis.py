import os
print("----- Welcome to the Dolphin terminal! ------")
print("You are running Dolphin version 1.4!\n")

print("Select a the Dolphin method you would like to use!")
print("[1] MANUAL MODE. This is perfect for users who want to use this on a personal computer. This mode has more features.")
print("[2] SERVER MODE. This is perfect for users who want to use this for a server to make videos with only 1 prompt at the start. Less features")
print("")
print("[3] Get help.")
print("[4] Exit")
pick = input(">>> ")

while 1:
    if pick == "1":
        os.system("bash ./launcher.sh")
        break
    elif pick == "2":
        os.system("python3 master.py")
        break
    elif pick == "3":
        print("To learn more about this product take a look at https://www.github.com/Ubuntufanboy/Dolphin.git and open an issue. I will be willing to help you")
        break
    elif pick == "4":
        print("Thank you for using Dolphin")
        exit()
    else:
        print("That is not a valid input! Please try again")