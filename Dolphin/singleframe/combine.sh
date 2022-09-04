RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

if ! ffmpeg -loop 1 -i img.jpg -i output.mp3 -shortest -acodec copy -vcodec mjpeg video.mp4 -hide_banner -loglevel error; then
    printf "Looks like you has a ${RED}FAILURE${NC}\n"
    exit
else
    printf "Your video has been created ${GREEN}sucsessfully${NC}\n"
fi

python3 upload_wizard.py
exit