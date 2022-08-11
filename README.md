# Dolphin
### An automatic video making software.

![Dolphin](Dolphin.png "Dolphin")
Dolphin is a framework where you can make videos fully automatically

Dolphin does this by allowing different modes for making certain types of videos.


## Installation

Find a youtube link for the audio and an image that you would like to overlay that audio file.

After that, run these following commands in order:

```bash
sudo apt update && sudo apt upgrade
sudo apt install git
git clone https://github.com/Ubuntufanboy/Dolphin
cd Dolphin/
chmod +x install.sh launcher.sh
./install.sh
```

Congrats! You have no installed all of the tools needed to run this program!

## Setting up YouTube API

Just as a warning or disclaimer, **Youtube will LOCK all of the videos you upload via the API due to youtube not verifying the API.** But if you *MANUALY* upload the videos to Youtube it will *NOT LOCK* the video.

### Follow the below steps to setup your API

1. Navigate to [Google Cloud](https://cloud.google.com/) and make an accout if you don't already have one.

2. Click on *CONSOLE* on the top bar near your google profile image.

3. On the left side of your screen you should see a option to make a new project called *"Select a project"* click on that.

4. Click on *New Project* and name it what ever you want (But it can **NOT** be changed later).

5. Click on the bell icon and once the project is done loading click on *"Select project"*.

6. On the left side on your screen you should see some options. Scroll down until you see *"Marketplace"* (It should be the 4th option) then click on it.

7. Type into the search bar *"Youtube Data API"* then select the first option. (At the time it is called "YouTube Data API v3") then click `Enable`.

8. Once it is done downloading it should take you to a new screen that is the API menu.

9. Click Oauth consent screen on the left side of your screen.

10. Select *"External"* and click create.

11. Fill out the fields that have a red star on then. They are required. Then scroll down and click *"Save and continue"*.

12. You should now be in a menu called *Scopes*. Click `Add or Remove scopes` then in the filter bar type "Upload" then press enter and select the first option that appears.

13. Click the check mark to the left of it and click `Update`. Scroll all the way to the bottom and click *"Save an continue"*.

14. You should now be in a menu called `Test users`. Click on "*Add users*" and type in the Gmail account that you would like to use the program with.

15. Click save and continue. Then scroll down and click "*Back to dashboard*".

16. Go to the left of your screen and click "Credentials" with the key icon. Then at the top click "*Create credentials*".

17. Click "API key" don't worry about it for now though. exit and click "Create credentials" again but this time click "Oauth client ID".

18. Click on the selector bar and select "Desktop app" and name it what ever you want because it doesn't matter really. Then click "*Create"*.

19. Write down the client ID and cliend secret and use the for later.

20. Run the following commands:
```bash
pip3 install --upgrade google-api-python-client
pip3 install --upgrade google-auth-oauthlib google-auth-httplib2
```

21. Open `client_secrets.json`.

22. Then replace *"[[ENTER CLIENT ID HERE]]"* with your actual Client ID that you wrote down (Make sure you keep the quotes there).

23. Do the same for *"[[ENTER CLIENT SECRET HERE]]"* (Make sure you keep the quotes there).

## Usage

- First run ``bash ./launcher.sh``

Depending on what mode you are going to use the instructions are a little different

### Copycat mode

This mode will take a video off YouTube and reupload it with your account

Rather simple to use. Just follow the instructions given to you.

### Video editor mode

This mode will take at least 2 video files and as many audio files as you want to make a video

Here are some helpful hints

- You must provide at least 1 audio file
- You must provide at least 2 video files
- The video files will not have their original audio but rather the audio of the audio files
- You must provide the full path of the files
- Try to only use mp4 and mp3 files
- This is very resource intensive so make sure you save any open documents in the event of a crash

### Single frame mode

Single frame mode is a mode that will take the audio of a youtube video and an image together to make a video that has 1 frame with the audio playing

Here are some helpful hints

- Make sure your image is named img.jpg
- You need to run ``chmod +x main.sh combine.sh``
- Follow the instructions given to you
- If a problem occurs create an issue so we can get to fixing the problem

## Contributing 

This framework is a powerful piece of tech. But 1 single person can't make a whole framework by themselves! Why not make a pull request to add a feature! Or maybe make a suggestion on the issue tab! 

### Thank you for reading! Have a nice day!
