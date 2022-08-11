#!/usr/bin/env bash

echo "Welcome to the auto-video-maker installer"
echo "This script will install all the required packages for this tool to work."
sleep 2
echo "Updating system..."
sudo apt update && sudo apt upgrade
echo "Giving executable perms..."
chmod +x main.sh combine.sh
echo "Installing ffmpeg..."
sudo apt install ffmpeg
echo "Installing yt-dlp..."
sudo apt install yt-dlp
echo "Installing mpv..."
sudo apt install mpv
echo "Installing python3..."
sudo apt install python3
echo "Installing termcolor..."
pip3 install termcolor
echo "Installing pedalboard..."
pip3 install pedalboard
echo "Installing oauth2client..."
pip3 install oauth2client
echo "Installing moviepy"
pip3 install moviepy
echo "Installing silver..."
wget https://raw.githubusercontent.com/Ubuntufanboy/Silver/main/silver.py

echo "The Installation has successfully finished."
