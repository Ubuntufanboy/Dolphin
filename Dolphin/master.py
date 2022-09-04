from os import system
print("This is the master file")
print("This is what will be used on the server to make videos!")
print("Follow this guide to set up the server:")
print("Have you already made a conf.dolphin file? If not, make one! (y/n)")
answer = input(">>> ")
if answer == "y":
    print("Great! Let's get started!")
else:
    print("You need to make a conf.dolphin file!")
    system("python3 dolphin_wizard.py")
    print("The conf.dolphin file has been created!")

print("Welcome to the server dashboard! What would you like to do?")
print("1. Initialize the server")
print("2. Get help")
print("3. See videos")
print("4. Exit")

mode = int(input(">>> "))
if mode == 1:
    system("bash ./inst.sh")
elif mode == 2:
    print("For help please check the README.md file! Or maybe the github page! Maybe if you are daring enough... You can contact the developer on discord! at Apolloiscool#7891 ")
elif mode == 3:
    system("ls")
elif mode == 4:
    print("Goodbye!")
    exit()
