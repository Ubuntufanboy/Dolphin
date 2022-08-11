from configparser import ConfigParser
config = ConfigParser()

try:
    config.read('settings.ini')
    download_bool = config.get('USER', 'youtube_download')

except:
    print("Hey! looks like you don't have the file settings.ini! Using default settings!...")
    download_bool = "TRUE"


if download_bool == "TRUE":
    pass

elif download_bool == "ASK":
    print("If you already have an audio file named \"Input.mp3\" you can skip this step")
    print("Would you like to skip the youtube link download? y/n")
    skip = input(">>> ")
    
    if skip == "y":
        exit()

    else:
        pass

elif download_bool == "FALSE":
    exit()

else:
    print("ERROR: Incorrect input! value must be \"TRUE\", \"ASK\", or \"FALSE\"")

import os
link = input("Enter the yt-link >>> ")
os.system(f"yt-dlp {link} -o input.opus -q -x")
os.system("ffmpeg -i input.opus input.mp3 -hide_banner -loglevel error")
