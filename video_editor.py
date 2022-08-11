# Layer an mp4 file and an mp3 file together
# Take in a video file and an audio file and layer them together
# import moviepy.editor as mpy
from os import system
import moviepy.editor as mpy

audioline = []
videoline = []

print("--- Welcome to the Video Editor! ---")

# Ask user for audio file
while 1:
    audio_file = input("Enter an AUDIO file to import into the media bin to start! enter \"exit\" to finish ")
    if audio_file == "exit":
        break
    # If file is a video then add to video line
    if audio_file.endswith(".mp4"):
        videoline.append(audio_file)
    else:
        audioline.append(audio_file)

# Ask user for video file
while 1:
    video_file = input("Enter a VIDEO file to import into the media bin to start! enter \"exit\" to finish ")
    if video_file == "exit":
        break
    if video_file.endswith(".mp4"):
        videoline.append(video_file)
    else:
        # Add to audio line
        audioline.append(video_file)

# Ask user for output file name
file_name = input("Exported file name >>> ")

# Combine the audio files into one audio file
# First make the files in audioline into clips
# Then combine them into one audio file
audio_clips = []
for i in range(len(audioline)):
    audio_clips.append(mpy.AudioFileClip(audioline[i]))

audio = mpy.concatenate_audioclips(audio_clips)

# Combine the video files into one video file
# Turn every file in video line into a clip
# Then combine them into one video file
video_clips = []
for i in range(len(videoline)):
    video_clips.append(mpy.VideoFileClip(videoline[i]))
video = mpy.concatenate_videoclips(video_clips, method="compose")

# Combine audio and video into one file
exported = mpy.CompositeVideoClip([video])
exported.audio = audio
# Export the file
exported.write_videofile(file_name)

# Inform the user that the file has been exported
print("Exported file name: " + file_name)
print("Video is finished! Would you like to watch the video? Y/n")
q = input(">>> ")
if q != "n":
    command = "mpv " + file_name
    system(command)
print("Would you like to upload the file to YouTube? Y/n")
q = input(">>> ")
if q != "n":
    command = "python3 upload_wizard.py"
    system(command)
print("Thank you for using the video editor!")