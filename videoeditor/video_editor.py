import moviepy.editor as mpy
from termcolor import colored
from os import system

clips = []
workline = []
timeline = []
audioline = []
print(colored("----- Welcome to the video editor! -----", color="blue"))

# Add files into media bin
while 1:
    file = input("Enter a file to import into the media bin to start! enter \"exit\" to finish ")
    if file == "exit" or file == " exit" or file == "exit ":
        pass
    else:
        clips.append(file)
    if file == "exit":
        break

while 1:
    print("Select a file to add to the timeline")
    #  This prints the menu
    for i in range(len(clips)):
        print(f"{i + 1}. {clips[i]}")
    print(f"{i + 2}. exit")
    choice = int(input("Select a number: "))
    if choice == (i + 2):
        break
    workline.append(clips[choice - 1])

    cut_diolog = input("Do you want to cut the clip? y/n ")
    if cut_diolog == "y":
        start_point = float(input("How many seconds in should the clip start? "))
        end_point = float(input("When should the clip end?"))
        video_dialog = input("Is this a video file y/n ")
        if video_dialog == "y":
            timeline.append(mpy.VideoFileClip(workline[-1]).subclip(start_point, end_point))
        elif video_dialog == "n":
            audioline.append(mpy.AudioFileClip(workline[-1]).subclip(start_point, end_point))
        else:
            print("Error wrong input!")
    elif cut_diolog == "n":
        video_dialog = input("Is this a video file y/n ")
        if video_dialog == "y":
            timeline.append(mpy.VideoFileClip(workline[-1]))
        elif video_dialog == "n":
            audioline.append(mpy.AudioFileClip(workline[-1]))
        else:
            print("Error wrong input!")

print("Exporting video...")
file_name = input("Exported file name >>> ")
exported = mpy.concatenate_videoclips(timeline, method="compose")
exported.audio = mpy.concatenate_audioclips(audioline)
exported.write_videofile(file_name)

print(colored("----- Exported! -----", color="green"))
print("Video has finished! Would you like to watch the video? Y/n")
watch = input(">>> ")

if watch == "y":
    system("mpv " + file_name)