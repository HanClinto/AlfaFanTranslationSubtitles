mkdir -p videos
cd videos
# This downloads all videos from the original playlist
yt-dlp --no-simulate --write-auto-subs --restrict-filenames --embed-thumbnail --embed-chapters --add-metadata --write-description https://www.youtube.com/playlist\?list\=PLCMefdkukgNB-AHT14KHjmb7um6I0XrIG
