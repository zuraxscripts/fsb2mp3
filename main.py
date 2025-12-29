import subprocess
from pathlib import Path

FSB_INPUT = Path("fsb_input")
MP3_OUTPUT = Path("mp3_output")

VGM = Path("vgmstream-cli.exe")

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def process_fsb(fsb):
    print(f"🎧 Converting: {fsb.name}")

    MP3_OUTPUT.mkdir(exist_ok=True)

    wav = MP3_OUTPUT / f"{fsb.stem}.wav"
    mp3 = MP3_OUTPUT / f"{fsb.stem}.mp3"

    run(f'"{VGM}" "{fsb}" -o "{wav}"')

    run(f'ffmpeg -y -i "{wav}" -q:a 0 "{mp3}"')

    wav.unlink()

def main():
    fsb_files = list(FSB_INPUT.glob("*.fsb"))
    if not fsb_files:
        print("⚠️ Unable to find any fsb files to convert")
        return

    for fsb in fsb_files:
        process_fsb(fsb)

    print("✅ COMPLETE")

if __name__ == "__main__":
    main()
