# 🎧 FSB to MP3 Converter (Python)

A simple Python script for **batch converting `.fsb` audio files to `.mp3`** using **vgmstream** and **FFmpeg**.

The script:
- scans the `fsb_input` folder for `.fsb` files
- converts them to `.wav`
- converts the WAV files to `.mp3`
- saves the final MP3 files into the `mp3_output` folder



## 📁 Project Structure

```

project/
├── fsb_input/        # input .fsb files
├── mp3_output/       # output .mp3 files (created automatically)
├── vgmstream-cli.exe # FSB decoding tool
├── convert.py        # main Python script

````



## ✅ Requirements

To run this script, you need the following:

### 1️⃣ Python 3.8+
Check your version:
```bash
python --version
````

Download Python if needed:
👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)



### 2️⃣ FFmpeg

FFmpeg must be:

* installed
* available in your **PATH**

Verify installation:

```bash
ffmpeg -version
```

Download (Windows):
👉 [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
Recommended: **static build**



### 3️⃣ vgmstream-cli

A tool used to decode `.fsb` audio files.

Steps:

* Download **vgmstream-cli**
* Rename it to `vgmstream-cli.exe`
* Place it in the project root directory

Download:
👉 [https://github.com/vgmstream/vgmstream/releases](https://github.com/vgmstream/vgmstream/releases)



## ▶️ Usage

1. Put all `.fsb` files into:

```
fsb_input/
```

2. Run the script:

```bash
python convert.py
```

3. Converted `.mp3` files will appear in:

```
mp3_output/
```



## ⚙️ MP3 Quality Settings

The script currently uses:

```bash
-q:a 2
```

Meaning:

* Very high-quality VBR MP3 (~190 kbps)

You can adjust this value:

* **Higher quality** → `-q:a 0`
* **Smaller file size** → `-q:a 4` to `-q:a 6`



## ❗ Troubleshooting

### ❌ `Unable to find any fsb files to convert`

➡️ The `fsb_input` directory is empty or contains no `.fsb` files



### ❌ `ffmpeg is not recognized`

➡️ FFmpeg is not added to PATH
➡️ Add it to system environment variables or use an absolute path



### ❌ `vgmstream-cli.exe not found`

➡️ The file is missing or renamed
➡️ Make sure it is located in the same directory as the script



## 📜 License

This script is provided **as-is**, without warranty, and is intended for personal and educational use only.

Please respect the licenses of the third-party tools used:

* FFmpeg
* vgmstream
