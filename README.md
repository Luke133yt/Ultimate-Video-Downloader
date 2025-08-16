# Ultimate Media Downloader (yt-dlp)
![UVD Logo](https://github.com/Luke133yt/Ultimate-Video-Downloader/assets/50149935/9ee65079-ae8a-4319-b26f-40ecf52fe6e9)

A Python application with a **CustomTkinter** GUI that allows you to download videos and audio from YouTube, Spotify, TikTok, Facebook, Instagram, and many more platforms using **yt-dlp**.

[WARNING] I've made this project just because i've always need a tool for downloading video or clip for my video and everytime that i need i pass like 2/3m on some suspiscious site that send the non copyrighted song or the clip that i need for my video and this is so stressfull because i can lost the workflow

---

## 🚀 Features
- Download YouTube videos in multiple resolutions
- Download audio only (MP3 format)
- Support for Facebook, Instagram, TikTok, and Spotify (via yt-dlp)
- Built-in progress bar
- Simple and intuitive GUI

---

## 📦 Requirements

- Python 3.9 or higher  
- Required Python libraries:
- Linux:
  ```bash
  pip install customtkinter yt-dlp
  ```
- Windows:
    ```bash
  py -m pip install customtkinter yt-dlp
  ```
- **FFmpeg** installed on your system (needed to merge audio/video and convert to MP3).

---

## 🔧 Installing FFmpeg on Windows

1. Download the FFmpeg release from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)  
   - Recommended: builds from **gyan.dev** or **BtbN**.  
2. Extract the downloaded folder (e.g., `ffmpeg-xxxx-win64`).  
3. Move the folder to a permanent location, for example:  
   ```
   C:\Program Files\ffmpeg
   ```  
4. Add `C:\Program Files\ffmpeg\bin` to the Windows **PATH** environment variable:  
   - Open the Start menu and search for *Environment Variables*.  
   - Click on **Environment Variables**.  
   - Select the `Path` variable and click **Edit**.  
   - Add the path: `C:\Program Files\ffmpeg\bin`  
   - Confirm with OK.  
5. Verify installation by opening the terminal (`cmd`) and typing:  
   ```bash
   ffmpeg -version
   ```  
   If the version appears → FFmpeg is correctly installed ✅

Just If you have no hands use this to install ffmpeg: https://github.com/oop7/ffmpeg-install-guide

---

## ▶️ Running the Program

Clone or download this repository, then run:

```bash
python main.py
```

The graphical application window will open.

---

## 🖥️ Usage

1. Paste the URL into the text field.  
2. Select the mode:  
   - **Download Video!** → Download the video (choose resolution).  
   - **Download Audio!** → Download audio only (in MP3).  
   - **Download from Facebook/Instagram/TikTok/Spotify!** → Download media from other platforms.  
3. Track progress in the progress bar.

---

## ⚠️ Important Notes

- The app uses **yt-dlp**, which is frequently updated. To stay safe, update with:  
  ```bash
  pip install -U yt-dlp
  ```
- Some platforms may change their APIs, so keep FFmpeg and Python up to date.  
- This application is intended for **personal use only**.

---

## 📜 License

This project is distributed under the MIT license. You are free to use, modify, and redistribute it.

If you need help or question contact me on Instagram (luca_cosini_2002) or Telegram (Luke133)
