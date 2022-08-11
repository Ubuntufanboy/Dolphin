from termcolor import colored
from os import system
from configparser import ConfigParser
config = ConfigParser()
try:
    config.read('settings.ini')
    download_bool = config.get('USER', 'youtube_upload')
except:
    download_bool = "ASK"

if download_bool == "TRUE":
    pass

elif download_bool == "ASK":
    print("Do you want to upload the video? y/n ")
    skip = input(">>> ")
    if skip == "n":
        exit()        
    else:
        pass

elif download_bool == "FALSE":
    exit()

else:
    print("ERROR: Incorrect input! value must be \"TRUE\", \"ASK\", or \"FALSE\"")

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
