RED='\033[1;31m'
GREEN='\033[1;32m'
NC='\033[0m' # No Color
printf "${RED} ----- Welcome to auto-video-maker! ----- ${NC}\n"
echo ''
echo ''
printf "${GREEN} ----- Please select a mode to use! ----- ${NC}\n"
echo ''
printf "${GREEN} 1.) Copy cat mode ${NC}\n"
printf "${GREEN} 2.) Video edit mode ${NC}\n"
printf "${GREEN} 3.) Single frame mode ${NC}\n"
echo ''
printf "# Choice -> "
read choice

if [ $choice == '1' ]; then
    python3 yt-copy.py
    exit
fi


if [$choice == '2' ]; then
    python3 video_editor.py
    exit
fi

if [$choice == '3' ]; then
    bash ./main.sh
    exit
fi 
