cd wavs

model_size=large
#model_size=medium

#task=translate
task=transcribe

output_dir="../srts_${task}_${model_size}"

mkdir -p "$output_dir"

for wavfile in *.wav; do
  output="${wavfile%.wav}.srt"
  
  #whisper "$wavfile" --language Indonesian --task "$task" --word_timestamps True --model "$model_size" --output_format srt --output_dir "$output_dir"
  whisper "$wavfile" --language Indonesian --task "$task" --model "$model_size" --output_format srt --output_dir "$output_dir"
  #~/github/whisper.cpp/main -f "$output" -osrt --language id --model ~/github/whisper.cpp/models/ggml-large.bin -tr -of "${file%.webm}.en"
  #~/github/whisper.cpp/main -f "$output" -osrt --language id --model ~/github/whisper.cpp/models/ggml-large.bin -tr -of "${file%.webm}.en"
done

#whisper ALFA_-_Episode_01-\[CBl51j1XOIM\].mkv.wav --language Indonesian --task translate --model large --output_format srt
#whisper ALFA_-_Episode_01-\[CBl51j1XOIM\].mkv.wav --language Indonesian --task translate --model medium --output_format srt
