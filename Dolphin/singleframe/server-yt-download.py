import os

os.chdir("..") # Move into the directory that has the conf.dolphin file
content = open("conf.dolphin", "r")
os.chdir("singleframe")
lines = []
for line in content:
    lines.append(line)
# Remove all of the lines that are not for this file
for line in lines: # for all the lines that are in conf.dolphin...
    listed = line.split() # Split it
    if listed[0] != "yt-download": # If it's not this file...
        lines.remove(line) # Remove it

# Get the yt-link
for i in range(len(lines)):
    if i == 0:
        line = lines[0]
        link = line.split()[2]
    else:
        break

os.system(f"yt-dlp {link} -o input.opus -q -x")
os.system("ffmpeg -i input.opus input.mp3 -hide_banner -loglevel error")
