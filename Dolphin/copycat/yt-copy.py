import os
this_file = [] # The conf.dolphin lines that is for this file
work_line = [] # Any conf.dolphin line

# We need to cd into the parent dir to find the conf.dolphin
os.chdir("..")
conf_file = open("conf.dolphin", "r")

# For good practice let's go back to the correct dir
os.chdir("copycat")

# Add the lines to work_line
for line in conf_file:
    work_line.append(line)

# Add the correct lines to this_file
for line in work_line:
    splited = line.split()
    if splited[0] == "yt-copy.py":
        this_file.append(line)

# Add the link in conf.dolphin
for line in this_file:
    splitted = line.split()
    if splitted[1] == "1":
        link = splitted[2]
    elif splitted[1] == "2":
        answer = splitted[2]
    else:
        pass
os.system(f"yt-dlp {link} -o video")
if answer == "y":
    os.system("python3 upload_wizard.py")
else:
    exit()
