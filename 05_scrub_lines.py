import sys
import re
import glob

remove_strings = [
    '[Music]',
    '[Music Playing]',
    'To be continued...',
]

def process_file(filename):
    print(f' Processing {filename}')
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Parsing srt file
    entries = []
    current_timestamp = None
    current_text = []
    for line in lines:
        line = line.strip()
        if "-->" in line:
            if current_timestamp and current_text:
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
