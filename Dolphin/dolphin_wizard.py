from os import system
import os
system("chmod +x inst.sh")
system("clear")


print("----- Welcome to the Dolphin Wisard! -----")

print("What mode would you like to use? 1. copycat 2. video editor 3. single frame 4. exit")
mode = int(input(">>> "))

if mode == 1:
    system("echo 'cd copycat && python3 yt-copy.py' > inst.sh")
    
    print("What YouTube link would you like to copy?")
    link = input(">>> ")
    
    command = f"echo 'yt-copy.py 1 {link}' >> conf.dolphin"
    system(command)

    print("Do you want to upload the video to youtube? (y/n)")
    answer = input(">>> ")
    if answer == "y":
        system("echo 'yt-copy.py 2 y' >> conf.dolphin")
    else:
        system("echo 'yt-copy.py 2 n' >> conf.dolphin")
        print("You are finished!")
        exit()

    pwd = os.getcwd()
    print(f"DEBUG: {pwd}")
    path = pwd + "/copycat/video.webm"

    system(f"echo 'upload_wizard.py 1 {path}' >> conf.dolphin")

    print("What would you like the title of the video to be?")
    title = input(">>> ")
    system(f"echo 'upload_wizard.py 2 {title}' >> conf.dolphin")

    print("What would you like the description of the video to be?")
    description = input(">>> ")
    system(f"echo 'upload_wizard.py 3 {description}' >> conf.dolphin")

    print("What would you like the tags of the video to be?")
    tags = input(">>> ")
    system(f"echo 'upload_wizard.py 4 {tags}' >> conf.dolphin")

    print("What would you like the privacy of the video to be?")
    privacy = input(">>> ")
    system(f"echo 'upload_wizard.py 5 {privacy}' >> conf.dolphin")

    print("What would you like the category of the video to be?")
    category = input(">>> ")
    system(f"echo 'upload_wizard.py 6 {category}' >> conf.dolphin")

    print("You are finished!")
    exit()
elif mode == 2:
    system("echo 'cd videoeditor && python3 server_editor.py' > inst.sh")

    print("How many files would you like to add to the media bin?")
    num_files = int(input(">>> "))
    for i in range(num_files):
        print(f"Enter the path to the {i+1} file:")
        path = input(">>> ")
        system(f"echo 'video_editor.py {i + 1} {path}' >> conf.dolphin")
    system(f"echo 'video_editor.py {i + 2} exit' >> conf.dolphin")
    
    print("What would you like the filename to be?")
    filename = input(">>> ")
    system(f"echo 'video_editor.py {i + 3} {filename}' >> conf.dolphin")

    print("Would you want to watch the video? * Recomended NO * (y/n)")
    answer = input(">>> ")
    if answer == "y":
        system(f"echo 'video_editor.py {i + 4} y' >> conf.dolphin")
    else:
        system(f"echo 'video_editor.py {i + 4} n' >> conf.dolphin")
        
elif mode == 3:
    system("echo 'cd singleframe && bash ./main.sh' > inst.sh")
    print("Enter the YouTube link:")
    link = input(">>> ")
    system(f"echo 'yt-download 1 {link}' >> conf.dolphin")
    print("Would you like to edit the audio of the video? (y/n)")
    answer = input(">>> ")
    if answer == "y":
        system("echo 'editor 1 y' >> conf.dolphin")
        print("Would you like to add the chours effect to the video? (y/n)")
        answer = input(">>> ")
        if answer == "y":
            system("echo 'editor 1 y' >> conf.dolphin")
        else:
            system("echo 'editor 1 n' >> conf.dolphin")

        print("Would you like to add the distortion effect to the video? (y/n)")
        answer = input(">>> ")
        if answer == "y":
            system("echo 'editor 2 y' >> conf.dolphin")
        else:
            system("echo 'editor 2 n' >> conf.dolphin")

        print("Would you like to add the phaser effect to the video? (y/n)")
        answer = input(">>> ")
        if answer == "y":
            system("echo 'editor 3 y' >> conf.dolphin")
        else:
            system("echo 'editor 3 n' >> conf.dolphin")

        print("Would you like to add the gain effect to the video? (y/n)")
        answer = input(">>> ")
        if answer == "y":
            system("echo 'editor 4 y' >> conf.dolphin")
        else:
            system("echo 'editor 4 n' >> conf.dolphin")
    
        print("Would you like to add the reverb effect to the video? (y/n)")
        answer = input(">>> ")
        if answer == "y":
            system("echo 'editor 5 y' >> conf.dolphin")
        else:
            system("echo 'editor 5 n' >> conf.dolphin")
        
        print("Would you like to add the pitch shift effect to the video? (y/n)")
        answer = input(">>> ")
        if answer == "y":
            system("echo 'editor 6 y' >> conf.dolphin")
            amount = int(input("How many semitones would you like to shift?"))
            system(f"echo 'editor 7 {amount}'>> conf.dolphin")
        else:
            system("echo 'editor 6 n' >> conf.dolphin")

    else:
        system("echo 'editor 1 n' >> conf.dolphin")
    
    print("Would you like to upload the video to YouTube? (y/n)")
    answer = input(">>> ")
    if answer == "y":
        system("echo 'combine 1 y' >> conf.dolphin")
    else:
        system("echo 'combine 1 n' >> conf.dolphin")
    
elif mode == 4:
    print("Exiting...")
    exit()
else:
    print("Error wrong input!")
    exit()

