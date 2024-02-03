'''
Made on 03/02/2024 at 14:06
By Luke133 with Love

This app allows you to download any media from the major media source online!
'''

#necessary for GUI
import customtkinter as ctk
from tkinter import ttk

#necessary for youtube video/audio downloading
from pytube import YouTube

#necessary for facebook download
import sys 
import youtube_dl 
import os

#necessary for instagram download
import instaloader

#necessary for tiktok download
#from tiktokapi import TikTokApi

#necessary for spotify
#download spotdl
#download FFMpeg

#REMOVE THE # FROM YOUR OPERATING SYSTEM:
operating_system = 'Windows'
#operating_system = 'Other' #Linux/MacOS

def download_YT(option):

    status_label = ctk.CTkLabel(content_frame, text="")

    progress_label.pack(pady=("10p" "5p"))
    progress_bar.pack(pady=("10p" "5p"))
    status_label.pack(pady=("10p" "5p"))

    try:

        url = entry_url.get()
        yt = YouTube(url, on_progress_callback=on_progress)

        #if you wanna download the video
        if option == "Download Video!":

            resolution = resolution_var.get()

            #print the title to check if is correct!
            status_label.configure(text=f"[VIDEO] {str(yt.title)}", text_color="black", fg_color="yellow")

            if resolution == "Best Quality":
                ys = yt.streams.get_highest_resolution()
            else:
                ys = yt.streams.filter(res=resolution, progressive=True).first()


        #if you wanna download the audio
        elif option == "Download Audio!":

            #print the title to check if is correct!
            status_label.configure(text=f"[AUDIO] {str(yt.title)}", text_color="black", fg_color="yellow")

            ys = yt.streams.get_audio_only()

        else:
            return
        
        if ys:
            ys.download()
            status_label.configure(text=f"Downloaded!", text_color="white", fg_color="green")

        elif resolution == "Choose Resolution!":
            status_label.configure(text=f"Please Choose a Resolution!", text_color="white", fg_color="red")

        else:
            status_label.configure(text=f"No stream found for the selected resolution.", text_color="white", fg_color="red")

    except Exception as e:
        
        #if someone doesn't put an url
        if url.startswith != "http":
            status_label.configure(text=f"Please paste a valid URL!", text_color="white", fg_color="red")
        else:
            status_label.configure(text=f"Error: {str(e)}", text_color="white", fg_color="red")

def download_FB():

    status_label = ctk.CTkLabel(content_frame, text="")
    
    progress_label.pack(pady=("10p" "5p"))
    progress_bar.pack(pady=("10p" "5p"))
    status_label.pack(pady=("10p" "5p"))

    try:
        # getting URL from the user
        url = entry_url.get()
        y = {"format": "best"}

        # start downloading the video using provided options
        with youtube_dl.YoutubeDL(y) as u: 
            status_label.configure(text=f"Downloading", text_color="white", fg_color="green")
            # download the video
            u.download([url])
            status_label.configure(text=f"Downloaded!", text_color="white", fg_color="green")

    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color="white", fg_color="red")

def download_IG():

    status_label = ctk.CTkLabel(content_frame, text="")

    progress_label.pack(pady=("10p" "5p"))
    progress_bar.pack(pady=("10p" "5p"))
    status_label.pack(pady=("10p" "5p"))

    url = entry_url.get()

    loader = instaloader.Instaloader()

    #if there isn't any link, he supposed you put the name of an account and you want the profile picture
    if url.startswith != "http":
        status_label.configure(text=f"Downloading!", text_color="black", fg_color="yellow")
        profile = instaloader.Profile.from_username(loader.context, url)
        loader.download_profile(profile.username, profile_pic_only=True)
        status_label.configure(text=f"PFP Downloaded!", text_color="white", fg_color="green")

    else:
        # extract teh name of the user from the ID of the post/reel from the URL
        try:
            context = instaloader.Context(loader.context)
            media = instaloader.Post.from_shortcode(context, instaloader.Post.get_shortcode_from_url(url))   
        except instaloader.exceptions.InstaloaderException:
            status_label.configure(text=f"Error: impossible to extract information!", text_color="white", fg_color="red")
            return

        status_label.configure(text=f"Downloading!", text_color="black", fg_color="yellow")

        # download reel or post
        if media.is_video:
            loader.download_videos([media], target=media.owner_username)
            status_label.configure(text=f"Picture Downloaded!", text_color="white", fg_color="green")
        else:
            loader.download_pictures([media], target=media.owner_username)
            status_label.configure(text=f"Video Downloaded!", text_color="white", fg_color="green")

def download_TT():

    
    status_label = ctk.CTkLabel(content_frame, text="")

    progress_label.pack(pady=("10p" "5p"))
    progress_bar.pack(pady=("10p" "5p"))
    status_label.pack(pady=("10p" "5p"))

    url = entry_url.get()
    api = TikTokApi()

    try:
        # extract ID from the video URL
        video_id = url.split("/")[3]

        status_label.configure(text=f"Downloading!", text_color="black", fg_color="yellow")

        # download the video
        video_data = api.get_tiktok_by_url(url)
        url = video_data['itemInfo']['itemStruct']['video']['playAddr']

        # Save it!
        with open(f"{video_id}.mp4", "wb") as video_file:
            video_file.write(api.get_bytes(url))

        status_label.configure(text=f"Downloaded!", text_color="white", fg_color="green")

    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color="white", fg_color="red")

def download_SP():
    
    status_label = ctk.CTkLabel(content_frame, text="")

    progress_label.pack(pady=("10p" "5p"))
    progress_bar.pack(pady=("10p" "5p"))
    status_label.pack(pady=("10p" "5p"))

    url = entry_url.get()

    status_label.configure(text=f"Downloading!", text_color="black", fg_color="yellow")

    try:
        if operating_system == 'Windows':
            os.system(f"py -m spotdl {url}")
            status_label.configure(text=f"Downloaded!", text_color="white", fg_color="green")

        else:
            os.system(f"python3 spotdl {url}")
            status_label.configure(text=f"Downloaded!", text_color="white", fg_color="green")

    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color="white", fg_color="red")

def on_progress(stream, chun, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_completed = bytes_downloaded / total_size * 100

    progress_label.configure(text = str(int(percentage_completed)) + "%")
    progress_label.update()

    progress_bar.set(float(percentage_completed / 100))

root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root.title("Ultimate Video Downloader")

#i try put a logo
"""
icon = "<PATH to the .ico file>"
root.iconbitmap(icon)
"""

root.geometry("720x480")
root.minsize(1000, 600)
root.maxsize(4096, 1080)

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

# url section
url_label = ctk.CTkLabel(content_frame, text="Paste your URL here: ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=("10p" "5p"))
entry_url.pack(pady=("10p" "5p"))

# download Video button section
download_button = ctk.CTkButton(content_frame, text="Download Video!", command=lambda: download_YT("Download Video!") )
download_button.pack(pady=("10p" "5p"))

# resolution section
resolution = ["Best Quality", "1080p", "720p", "360p", "240p", "144p"]
resolution_var = ctk.StringVar()

resolution_combobox = ttk.Combobox(content_frame, values=resolution, textvariable=resolution_var, font=('Arial', 15), width=40)
resolution_combobox.pack(pady=("10p" "5p"))
resolution_combobox.set("Choose Resolution!")

# download Audio button section
download_button = ctk.CTkButton(content_frame, text="Download Audio!", command=lambda: download_YT("Download Audio!") )
download_button.pack(pady=("10p" "5p"))

# download Video from Facebook button section
download_button = ctk.CTkButton(content_frame, text="Download Best Quality Video from FB!", command=download_FB)
download_button.pack(pady=("10p" "5p"))

# download PFP, Reel or Video from Instagram button section
#past the name of the user if you want just the PFP or JIC put the url of a post/reels and it starts download
download_button = ctk.CTkButton(content_frame, text="Download Anything from IG!", command=download_IG)
download_button.pack(pady=("10p" "5p"))

# download Video from TikTok button section
download_button = ctk.CTkButton(content_frame, text="Download TikTok Video!", command=download_TT)
download_button.pack(pady=("10p" "5p"))

# download Music from Spotify button section
download_button = ctk.CTkButton(content_frame, text="Download from Spotify!", command=download_SP)
download_button.pack(pady=("10p" "5p"))

# progress bar section
progress_label = ctk.CTkLabel(content_frame, text="0%")

progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)
progress_label.pack(pady=("10p" "5p"))

root.mainloop()

#KNOWN ISSUES

'''
- Status bar works only for YT video/audio download, not fot the other
- The GUI is ugly ASF
- Probabbly i can make only a button without the menu for downloading youtube video and so make it more minimal
- sometimes te debug print on the app doesn't display, but it works!
- in download_IG function it doesn't work the download of the video or picture, just the PFP
- downloading from tiktok doesn't work
'''
