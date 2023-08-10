cd videos
#model=~/github/whisper.cpp/models/ggml-large.bin
#model=~/github/whisper.cpp/models/ggml-medium.bin
#model=~/github/whisper.cpp/models/ggml-small.bin

for file in *.mkv; do
  output="${file%.webm}.wav"
  ffmpeg -y -i "$file" -acodec pcm_s16le -ar 16000 "../wavs/$output"
  #whisper "$output" --language Indonesian --task translate --model large --output_format srt
  #~/github/whisper.cpp/main -f "$output" -osrt --language id --model ~/github/whisper.cpp/models/ggml-large.bin -tr -of "${file%.webm}.en"
  #~/github/whisper.cpp/main -f "$output" -osrt --language id --model ~/github/whisper.cpp/models/ggml-large.bin -tr -of "${file%.webm}.en"
  #mv "$output" "../wavs/$output"
  #mv "$file" "./done/$file"
  #mv "${file%.webm}.en.srt" "./done/${file%.webm}.en.srt"
  #rm "$output"
done

#whisper ALFA_-_Episode_01-\[CBl51j1XOIM\].mkv.wav --language Indonesian --task translate --model large --output_format srt
#whisper ALFA_-_Episode_01-\[CBl51j1XOIM\].mkv.wav --language Indonesian --task translate --model medium --output_format srt
