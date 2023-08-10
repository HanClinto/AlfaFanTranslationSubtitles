import sys
import re
import glob

remove_strings = [
    '[Music]',
    '[Music Playing]',
    'To be continued...',
]

substitute_strings = {
    'Alva': 'Alfa',
    'ALVA': 'ALFA',
}

automatic_intro = [
    [
    '00:00:00,000 --> 00:00:05,000',
    'This story is purely fictional. If there are similarities in names, characters/figures, and places in this show, it is merely a coincidence without any element of intentionality.',
    ],[
    '00:00:14,000 --> 00:00:16,000',
    'MDentertainment presents',
    ],[
    '00:00:22,000 --> 00:00:28,000',
    '🎵 "Show your spirit, get your friends ready" 🎵',
    ],[
    '00:00:28,000 --> 00:00:35,000',
    '🎵 "Run, jump, jump, conquer the stars" 🎵',
    ],[
    '00:00:35,000 --> 00:00:42,000',
    '🎵 "Be brave, don\'t give up" 🎵',
    ],[
    '00:00:42,000 --> 00:00:49,000',
    '🎵 "Chase your dreams and hopes" 🎵',
    ],[
    '00:00:50,000 --> 00:00:53,000',
    '🎵 "Go, go, go, achieve all your dreams" 🎵',
    ],[
    '00:00:53,000 --> 00:00:56,000',
    '🎵 "Go, go, go, never stop" 🎵',
    ],[
    '00:00:56,000 --> 00:01:02,000',
    '🎵 "Go, go, go, fight with all your heart" 🎵',
    ],[
    '00:01:02,000 --> 00:01:06,000',
    '🎵 "Go, go, go, make yourself proud" 🎵',
    ],[
    '00:01:06,000 --> 00:01:10,000',
    '🎵 "Go, go, go, let\'s dream" 🎵',
    ],[
    '00:01:10,000 --> 00:01:15,000',
    '🎵 "Go, go, go, we can do it" 🎵',
    ],[
    '00:01:15,000 --> 00:01:19,000',
    '🎵 "We can do it!" 🎵',]
]

do_auto_intro = False

def process_file(filename):
    print(f' Processing {filename}')
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Parsing srt file
    entries = []

    if do_auto_intro:
        # Get the last timestamp of the intro
        last_intro_timestamp = automatic_intro[-1][0]
        # Adding automatic intro
        for timestamp, text in automatic_intro:
            entries.append((timestamp, text))

    current_timestamp = None
    current_text = []
    for line in lines:
        line = line.strip()
        if "-->" in line:
            if current_timestamp and current_text:
                if do_auto_intro and current_timestamp < last_intro_timestamp:
                    print(f'  Skipping {current_timestamp} {current_text}')
                else:
                    entries.append((current_timestamp, " ".join(current_text)))
                current_text = []
            current_timestamp = line
        elif line.isdigit() or not line:
            continue
        else:
            # Skip over lines if they are in the ignored list
            if line in remove_strings:
                print(f'  Skipping {line}')
                continue
            # Substitute strings
            for key, value in substitute_strings.items():
                line = line.replace(key, value)
            current_text.append(line.strip())
    if current_timestamp and current_text:
        entries.append((current_timestamp, " ".join(current_text)))

    # Merging consecutive entries with the same text
    merged = []
    prev_text = None
    prev_start = None
    prev_end = None
    for timestamp, text in entries:
        start, end = timestamp.split(" --> ")
        if text == prev_text:
            prev_end = end
            print(f'  Merging {prev_start} --> {prev_end} {text}')
        else:
            if prev_text is not None:
                merged.append((f"{prev_start} --> {prev_end}", prev_text))
            prev_text = text
            prev_start = start
            prev_end = end
    if prev_text is not None:
        merged.append((f"{prev_start} --> {prev_end}", prev_text))

    # Writing back to file
    with open(filename, 'w', encoding='utf-8') as file:
        for idx, (timestamp, text) in enumerate(merged, 1):
            file.write(f"{idx}\n{timestamp}\n{text}\n\n")


    # Also write to a simple txt file with just the entries
    with open(filename + ".txt", 'w', encoding='utf-8') as file:
        for idx, (timestamp, text) in enumerate(merged, 1):
            file.write(f"{idx}: {text}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: script.py <path>")
        return

    files = glob.glob(sys.argv[1])
    print(f'Processing {len(files)} files')
    for filename in files:
        print(f'Processing {filename}')
        process_file(filename)

if __name__ == "__main__":
    main()
