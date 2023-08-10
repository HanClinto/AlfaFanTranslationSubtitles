for file in *.webm; do
  output="${file%.webm}.wav"
  ffmpeg -i "$file" -acodec pcm_s16le -ar 16000 "$output"
  ~/github/whisper.cpp/main -f "$output" -osrt --language id --model ~/github/whisper.cpp/models/ggml-large.bin -tr -of "${file%.webm}.en"
  mv "$file" "./done/$file"
  mv "${file%.webm}.en.srt" "./done/${file%.webm}.en.srt"
  rm "$output"
done