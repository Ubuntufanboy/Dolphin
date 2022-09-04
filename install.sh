# Update packages
sudo apt-get update && sudo apt-get upgrade

# Python stuff
sudo apt install python3
sudo apt install python3-pip

# multimedia stuff
sudo apt install yt-dlp
sudo apt install mpv
sudo apt install ffmpeg

# pip packages
pip3 install moviepy
pip3 install playsound
pip3 install termcolor
pip3 install pedalboard
pip3 install oauth2client

# install silver
wget https://raw.githubusercontent.com/Ubuntufanboy/Silver/main/silver.py

# adding exec perms to shell files
cd Dolphin
chmod +x inst.sh
chmod +x launcher.sh
cd singleframe
chmod +x main.sh
chmod +x combine2.sh
chmod +x combine.sh
cd ..
cd ..
echo ''
echo 'Finished installing!'