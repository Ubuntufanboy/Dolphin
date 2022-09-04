import os
link = input("enter link here >>> ")

os.system(f"yt-dlp {link} -o video")

print("Would you like to upload the video to youtube?")
answer = input(">>> ")
if answer == "y":
    os.system("python3 upload_wizard.py")
else:
    exit()
