'''
Made on 03/02/2024 at 14:06
By Luke133 with Love

This app allows you to download any media from the major media source online!
'''

'''
Ultimate Media Downloader (fixed)
Uses yt-dlp instead of pytube/spotdl/youtube_dl
''' 

import customtkinter as ctk
from tkinter import ttk
from yt_dlp import YoutubeDL
import shutil

# --------------------- DOWNLOAD HANDLER ---------------------

def download_media(mode):
    status_label = ctk.CTkLabel(content_frame, text="")
    progress_label.pack(pady=5)
    progress_bar.pack(pady=5)
    status_label.pack(pady=5)

    url = entry_url.get()

    # Controllo se ffmpeg è installato
    if shutil.which("ffmpeg") is None:
        status_label.configure(text="Error: FFmpeg non trovato! Installalo per scaricare correttamente.", text_color="white", fg_color="red")
        return

    try:
        # Impostazioni base
        ydl_opts = {
            "progress_hooks": [lambda d: on_progress_hook(d)],
            "outtmpl": "%(title)s.%(ext)s",
            "merge_output_format": "mp4"  # forza uscita in mp4 se serve merging
        }

        # Modalità video
        if mode == "video":
            resolution = resolution_var.get()
            if resolution == "Best Quality" or resolution == "Choose Resolution!":
                ydl_opts["format"] = "bestvideo+bestaudio/best"
            else:
                ydl_opts["format"] = f"bestvideo[height={resolution[:-1]}]+bestaudio/best"
            status_label.configure(text="[VIDEO] Downloading...", text_color="black", fg_color="yellow")

        # Modalità audio
        elif mode == "audio":
            ydl_opts["format"] = "bestaudio/best"
            ydl_opts["postprocessors"] = [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }]
            status_label.configure(text="[AUDIO] Downloading...", text_color="black", fg_color="yellow")

        # Modalità generica (FB, IG, TikTok, Spotify ecc.)
        elif mode == "generic":
            ydl_opts["format"] = "best"
            status_label.configure(text="[GENERIC] Downloading...", text_color="black", fg_color="yellow")

        else:
            status_label.configure(text="Error: invalid mode", text_color="white", fg_color="red")
            return

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        status_label.configure(text="Downloaded!", text_color="white", fg_color="green")

    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color="white", fg_color="red")

# --------------------- PROGRESS BAR ---------------------

def on_progress_hook(d):
    if d['status'] == 'downloading':
        percent = d.get('_percent_str', '0%')
        progress_label.configure(text=percent)
        try:
            progress = float(percent.strip('%')) / 100
            progress_bar.set(progress)
        except:
            pass

# --------------------- GUI ---------------------

root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root.title("Ultimate Media Downloader (yt-dlp)")
root.geometry("720x480")
root.minsize(1000, 600)
root.maxsize(4096, 1080)

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# URL input
url_label = ctk.CTkLabel(content_frame, text="Paste your URL here: ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=5)
entry_url.pack(pady=5)

# YouTube Video button
download_button = ctk.CTkButton(content_frame, text="Download Video!", command=lambda: download_media("video"))
download_button.pack(pady=5)

# Resolution selector
resolution = ["Best Quality", "1080p", "720p", "360p", "240p", "144p"]
resolution_var = ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolution, textvariable=resolution_var, font=('Arial', 15), width=40)
resolution_combobox.pack(pady=5)
resolution_combobox.set("Choose Resolution!")

# YouTube Audio button
download_button = ctk.CTkButton(content_frame, text="Download Audio!", command=lambda: download_media("audio"))
download_button.pack(pady=5)

# Generic download buttons (FB, IG, TikTok, Spotify)
download_button = ctk.CTkButton(content_frame, text="Download from Facebook!", command=lambda: download_media("generic"))
download_button.pack(pady=5)

download_button = ctk.CTkButton(content_frame, text="Download from Instagram!", command=lambda: download_media("generic"))
download_button.pack(pady=5)

download_button = ctk.CTkButton(content_frame, text="Download from TikTok!", command=lambda: download_media("generic"))
download_button.pack(pady=5)

download_button = ctk.CTkButton(content_frame, text="Download from Spotify!", command=lambda: download_media("generic"))
download_button.pack(pady=5)

# Progress bar
progress_label = ctk.CTkLabel(content_frame, text="0%")
progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)
progress_label.pack(pady=5)

root.mainloop()

'''
KNOWN ISUES:

- Progress bar doesn't work anymore
- Spotify DRM error
- Tiktok needs log-in
'''
