RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

if ! ffmpeg -loop 1 -i img.jpg -i output.mp3 -shortest -acodec copy -vcodec mjpeg video.mp4 -hide_banner -loglevel error; then
    printf "Looks like you has a ${RED}FAILURE${NC}\n"
    exit
else
    printf "Your video has been created ${GREEN}sucsessfully${NC}\n"
fi


echo "Would you like to upload your video to youtube? y/n"
read n
if [ $n == 'y' ]; then
    python3 upload_wizard.py
    exit
fi


echo "Would you like to watch the video? y/n"
read n
if [ $n == 'y' ]; then
    mpv video.mp4
    exit
fi