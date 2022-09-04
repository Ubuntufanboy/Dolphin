import os
os.chdir("..") # Move into the directory that has the conf.dolphin file
content = open("conf.dolphin", "r")
os.chdir("singleframe")

lines = []

for line in content:
    lines.append(line)
lines_2 = lines
# See if user wants to edit audio...
for line in lines:
    splitted = line.split()
    if splitted[1] == "1":
        skip = splitted[2]
        lines.remove(line)
if skip == "n":
    last = lines[-1]
    splited = last.split()
    if splited[-1] == "y":
        os.system("bash ./combine.sh")
    else:
        os.system("bash ./combine2.sh")
else:
    # Remove all of the lines that are not for this file
    for line in lines_2: # for all the lines that are in conf.dolphin...
        listed = line.split() # Split it
        if listed[0] != "editor": # If it's not this file...
            lines_2.remove(line) # Remove it


#Start program
try:
    from pedalboard import Chorus, Distortion, Phaser, Gain, Reverb, PitchShift, Pedalboard
    from pedalboard.io import AudioFile
except ImportError:
    print("Hey! Pedalboard is not installed! Do you want to install it? y/n")
    while 1:
        answer = input(">>> ")
        if answer == "y":
            os.system("pip3 install pedalboard")
            break
        elif answer == "n":
            print("Well, this tool is very dependant on pedalboard so you will encounter errors!")
            break
        else:
            print("Wrong input!")

os.system("ffmpeg -i input.mp3 audio.wav -hide_banner -loglevel error")

with AudioFile('audio.wav', 'r') as f:
    audio = f.read(f.frames)
    samplerate = f.samplerate

board = Pedalboard([])

os.chdir("..") # Move into the directory that has the conf.dolphin file
content = open("conf.dolphin", "r")
os.chdir("singleframe")
lines_3 = []

os.chdir("..")
content_2 = open("conf.dolphin",'r')
for line in content_2:
    lines_3.append(line)
os.chdir("singleframe")

# Remove all of the lines that are not for this file
for line in lines_3: # for all the lines that are in conf.dolphin...
    listed = line.split() # Split it
    if listed[0] != "editor": # If it's not this file...
        lines_3.remove(line) # Remove it

lines_4 = lines_3
answers = []
for line in lines_3:
    split = line.split()
    answers.append(split[2])

while 1:
    chorus = answers[0]
    if chorus == "y":
        c = Chorus()
        board.append(c)        
        effected = board(audio, samplerate)
        with AudioFile('demo1.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)        
            break
    elif chorus == "n":
        break

while 1:
    distortion = answers[1]
    if distortion == "y":
        d = Distortion()
        board.append(d)
        effected = board(audio, samplerate)
        with AudioFile('demo2.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
            break
    elif distortion == "n":
        break

while 1:
    phaser = answers[2]
    if phaser == "y":
        p = Phaser()
        board.append(p)
        effected = board(audio, samplerate)
        with AudioFile('demo3.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
            break
    elif phaser == "n":
        break

while 1:
    gain = answers[3]
    if gain == "y":
        amount = 5
        gaindb = amount
        g = Gain(gaindb)
        board.append(g)        
        effected = board(audio, samplerate)
        with AudioFile('demo4.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)        
            break
    elif gain == "n":
        break

while 1:
    reverb = answers[4]
    if reverb == "y":
        re = Reverb(room_size=0.25)
        board.append(re)
        
        effected = board(audio, samplerate)
        with AudioFile('demo5.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
            break
    elif reverb == "n":
        break
while 1:
    pitch = answers[5]
    if pitch == "y":
        semis = answers[7]
        semis = float(semis)
        pi = PitchShift(semis)
        board.append(pi)
        effected = board(audio, samplerate)
        with AudioFile('demo6.wav', 'w', samplerate, effected.shape[0]) as f:
            f.write(effected)
            break
    elif pitch == "n":
        break
if os.path.exists("demo6.wav"):
    os.system("ffmpeg -i demo6.wav output.mp3 -hide_banner -loglevel error")
elif os.path.exists("demo5.wav"):
    os.system("ffmpeg -i demo5.wav output.mp3 -hide_banner -loglevel error")
elif os.path.exists("demo4.wav"):
    os.system("ffmpeg -i demo4.wav output.mp3 -hide_banner -loglevel error")
elif os.path.exists("demo3.wav"):
    os.system("ffmpeg -i demo3.wav output.mp3 -hide_banner -loglevel error")
elif os.path.exists("demo2.wav"):
    os.system("ffmpeg -i demo2.wav output.mp3 -hide_banner -loglevel error")
elif os.path.exists("demo1.wav"):
    os.system("ffmpeg -i demo1.wav output.mp3 -hide_banner -loglevel error")
else:
    print("Not audio edited!")

if os.path.exists("/home/apollo/GitHub/auto-video-maker/Testing-Dolphin/singleframe/demo1.wav"):
    os.system("rm demo1.wav")

if os.path.exists("demo2.wav"):
    os.system("rm demo2.wav")

if os.path.exists("demo3.wav"):
    os.system("rm demo3.wav")

if os.path.exists("demo4.wav"):
    os.system("rm demo4.wav")

if os.path.exists("demo5.wav"):
    os.system("rm demo5.wav")

if os.path.exists("demo6.wav"):
    os.system("rm demo 6.wav")

last = lines_4[-1]
splited = last.split()
if splited[2] == "y":
    os.system("bash ./combine.sh")
else:
    os.system("bash ./combine2.sh")
