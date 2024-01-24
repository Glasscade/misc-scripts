# Script for extracting the Cover Art from .mp3 files.

import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, error

def extract_cover_art(directory):
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            file_path = os.path.join(directory, file)
            try:
                audio = MP3(file_path, ID3=ID3)
            except error:
                print(f"Skipping file (ID3 tag not found): {file}")
                continue

            if "APIC:" in audio.tags:
                albumart = audio.tags["APIC:"].data
                with open(os.path.join(directory, f"{file[:-4]}_cover.jpg"), "wb") as img:
                    img.write(albumart)
                    print(f"Cover art extracted from {file}")
            else:
                print(f"No cover art found in {file}")

directory_path = r'C:\Music Library\Downloads\complete\telepath - telenightcore Vol 1' # Album File Path
extract_cover_art(directory_path)
