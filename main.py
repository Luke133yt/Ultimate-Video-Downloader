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
import threading
import re

# --------------------- HELPERS ---------------------

def detect_platform(url: str) -> str:
    """Rileva la piattaforma dal link"""
    if "youtube.com" in url or "youtu.be" in url:
        return "YouTube"
    elif "facebook.com" in url:
        return "Facebook"
    elif "instagram.com" in url:
        return "Instagram"
    elif "tiktok.com" in url:
        return "TikTok"
    elif "spotify.com" in url:
        return "Spotify"
    return "Unknown"

def update_quality_options():
    """Aggiorna la combobox in base alla modalità scelta"""
    if mode_var.get() == "audio":
        quality_combobox.configure(values=["128", "192", "256", "320"])
        quality_combobox.set("320")
    else:
        quality_combobox.configure(values=["Best", "1080p", "720p", "480p", "360p", "240p", "144p"])
        quality_combobox.set("Best")


def is_spotify_drm(url):
    """Controlla se il link Spotify è protetto da DRM"""
    # Nota: yt-dlp non scarica contenuti DRM, quindi simuliamo il check tramite eccezione
    if "spotify.com" in url:
        try:
            with YoutubeDL({'quiet': True}) as ydl:
                info = ydl.extract_info(url, download=False)
                if info.get('is_drm_protected'):
                    return True
        except Exception:
            return True
    return False


# --------------------- DOWNLOAD HANDLER ---------------------

def start_download():
    """Avvia il download in un thread separato"""
    url = entry_url.get().strip()
    if not url:
        status_label.configure(text="Inserisci un URL!", text_color="white", fg_color="red")
        return

    # Rilevo piattaforma
    platform = detect_platform(url)
    platform_label.configure(text=f"Detected: {platform}")

    mode = mode_var.get()
    quality = quality_combobox.get()

    thread = threading.Thread(target=download_media, args=(mode, quality))
    thread.start()

def download_media(mode, quality):
    url = entry_url.get().strip()

    if shutil.which("ffmpeg") is None:
        status_label.configure(
            text="Error: FFmpeg non trovato! Installalo per scaricare correttamente.",
            text_color="white", fg_color="red"
        )
        return

    # Controllo DRM Spotify
    if "spotify.com" in url and is_spotify_drm(url):
        status_label.configure(text="Spotify audio protetto da DRM! Download non consentito.", text_color="white", fg_color="red")
        return

    ydl_opts = {
        "progress_hooks": [lambda d: on_progress_hook(d)],
        "outtmpl": "%(title)s.%(ext)s",
        "merge_output_format": "mp4"
    }


    try:
        # Impostazioni base
        ydl_opts = {
            "progress_hooks": [lambda d: on_progress_hook(d)],
            "outtmpl": "%(title)s.%(ext)s",
            "merge_output_format": "mp4"
        }

        # Modalità video
        if mode == "video":
            if quality.lower() == "best":
                ydl_opts["format"] = "bestvideo+bestaudio/best"
            else:
                q = re.sub("[^0-9]", "", quality)  # estrae numeri da "720p"
                ydl_opts["format"] = f"bestvideo[height={q}]+bestaudio/best"
            status_label.configure(text=f"[VIDEO] Downloading {quality}...", text_color="black", fg_color="yellow")

        # Modalità audio
        elif mode == "audio":
            q = quality if quality.isdigit() else "320"
            ydl_opts["format"] = "bestaudio/best"
            ydl_opts["postprocessors"] = [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": q,
            }]
            ydl_opts["keepvideo"] = False
            status_label.configure(text=f"[AUDIO] Downloading {q}kbps...", text_color="black", fg_color="yellow")

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        status_label.configure(text="Downloaded!", text_color="white", fg_color="green")

    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color="white", fg_color="red")

# --------------------- PROGRESS BAR ---------------------

def on_progress_hook(d):
    if d['status'] == 'downloading':
        downloaded = d.get("downloaded_bytes", 0)
        total = d.get("total_bytes") or d.get("total_bytes_estimate") or 1
        percent = downloaded / total

        # Aggiorna barra
        progress_bar.set(percent)
        progress_label.configure(text=f"{percent*100:.2f}%")

        root.update_idletasks()

# --------------------- THEME SWITCHER ---------------------

def change_theme(choice):
    ctk.set_appearance_mode(choice)

# --------------------- GUI ---------------------

root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root.title("Ultimate Media Downloader (yt-dlp)")
root.geometry("900x600")
root.minsize(900, 600)

content_frame = ctk.CTkFrame(root, corner_radius=20)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=20)

# Titolo
title_label = ctk.CTkLabel(content_frame, text="🎵 Ultimate Media Downloader 🎬", font=("Arial", 28, "bold"))
title_label.pack(pady=15)

# URL input
url_label = ctk.CTkLabel(content_frame, text="Paste your URL here: ", font=("Arial", 16))
entry_url = ctk.CTkEntry(content_frame, width=500, height=40, font=("Arial", 14))
url_label.pack(pady=5)
entry_url.pack(pady=5)

# Piattaforma rilevata
platform_label = ctk.CTkLabel(content_frame, text="Detected: ---", font=("Arial", 14, "italic"))
platform_label.pack(pady=5)

# Scelta modalità (Audio/Video)
mode_var = ctk.StringVar(value="audio")

mode_frame = ctk.CTkFrame(content_frame, corner_radius=10)
mode_frame.pack(pady=10)

mode_label = ctk.CTkLabel(mode_frame, text="Choose Mode:", font=("Arial", 14))
mode_label.pack(side="left", padx=10)

radio_audio = ctk.CTkRadioButton(mode_frame, text="Audio", variable=mode_var, value="audio", command=update_quality_options)
radio_audio.pack(side="left", padx=10)

radio_video = ctk.CTkRadioButton(mode_frame, text="Video", variable=mode_var, value="video", command=update_quality_options)
radio_video.pack(side="left", padx=10)

# Selettore qualità
quality_combobox = ctk.CTkComboBox(content_frame, values=["320"], font=("Arial", 14))
quality_combobox.pack(pady=10)
quality_combobox.set("320")

# Pulsante unico download
download_button = ctk.CTkButton(content_frame, text="⬇️ Download", height=50, width=200, font=("Arial", 18, "bold"), command=start_download)
download_button.pack(pady=20)

# Progress bar + status
progress_label = ctk.CTkLabel(content_frame, text="0%", font=("Arial", 14))
progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)
status_label = ctk.CTkLabel(content_frame, text="", width=400, font=("Arial", 14))

progress_label.pack(pady=5)
progress_bar.pack(pady=5)
status_label.pack(pady=5)

# Selettore tema (in basso a destra)
theme_frame = ctk.CTkFrame(root, corner_radius=10)
theme_frame.place(relx=1.0, rely=1.0, anchor="se", x=-20, y=-20)

theme_label = ctk.CTkLabel(theme_frame, text="Theme:")
theme_label.pack(side="left", padx=5)

theme_menu = ctk.CTkOptionMenu(theme_frame, values=["System", "Light", "Dark"], command=change_theme)
theme_menu.pack(side="left", padx=5)
theme_menu.set("System")

# Imposta qualità iniziale in base alla modalità
update_quality_options()

root.mainloop()
