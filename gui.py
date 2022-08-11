from os import system
import PySimpleGUI as pg
from silver import Silver

layout = [
    [pg.Text("Welcome to auto-video-maker! What would you like to do?")],
    [pg.Text("")],
    [pg.Text("a) Download my audio from youtube! (Insert youtube link)->"), pg.InputText(key='-YOUTUBE_LINK-'), pg.Button("Download", key='-BUTTON1-')],
    [pg.Text("---")],
    [pg.Text("b) I already have an audio file! ->"), pg.InputText(key='-AUDIO_FILE-'), pg.FileBrowse(), pg.Button("Upload", key='-BUTTON2-')]
]

window = pg.Window('My app', layout)

while 1:
    event, values = window.read()
    if event == pg.WIN_CLOSED:
        break
    if event == "-BUTTON1-":
        link = values["-YOUTUBE_LINK-"]
        print("Downloading...")
        system(f"yt-dlp {link} -o input.mp3")
        system("ffmpeg -i input.mp3.opus input.mp3 -hide_banner -loglevel error")
    if event == "-BUTTON2-":
        file = values["-AUDIO_FILE-"]
        Silver.play(file)
# window.close()