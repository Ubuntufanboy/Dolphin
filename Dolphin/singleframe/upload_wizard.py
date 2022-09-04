from os import system
try:
    from termcolor import colored
except ImportError:
    print("termcolor needs to be installed! Install it? y/n")
    while 1:
        answer = input(">>> ")
        if answer == "y":
            system("pip3 install termcolor")
            break
        elif answer == "n":
            print("Dude...")
            break
        else:
            print("Wrong input!")
    
msg = colored("Youtube", "red")
msg = f"----- Welcome to the {msg} uploader! -----"
print(msg)
print("")
path = input("What is the video path? ")
print("")
title = input("What do you want the title to be? ")
print("")
des = input("What do you want the description to be? ")
print("")
print("Just as a bit of a warning. The tags are broken in this version.")
tags = input("What should the tags be? ")
print("")

while 1:
    sec = input("Do you want the video to be public? (This doesent matter because youtube locks the video anyway) ")
    if sec == "y" or sec == "n":
        break
    else:
        print("That isnt valid")

if sec == "y":
    stats = "public"
else:
    stats = "private"

command = f"python3 upload_video.py --file=\"{path}\" --title=\"{title}\" --description=\"{des}\" --keywords=\"{tags}\" --category \"22\" --privacyStatus=\"{stats}\""
print(command)
system(command)
