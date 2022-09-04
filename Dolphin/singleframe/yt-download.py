from os import system
link = input("Enter the yt-link >>> ")
system(f"yt-dlp {link} -o input.opus -q -x")
system("ffmpeg -i input.opus input.mp3 -hide_banner -loglevel error")
