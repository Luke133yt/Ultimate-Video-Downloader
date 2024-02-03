# Ultimate-Video-Downloader
A Multi Media Downloader, that can download from Youtube, Spotify, TikTok, Isntagram, Facebook

![UVD Logo](https://github.com/Luke133yt/Ultimate-Video-Downloader/assets/50149935/9ee65079-ae8a-4319-b26f-40ecf52fe6e9)

[WARNING] I've made this project just because i've always need a tool for downloading video or clip for my video and everytime that i need i pass like 2/3m on some suspiscious site that send the non copyrighted song or the clip that i need for my video and this is so stressfull because i can lost the workflow

so i lost a few hours to make this tool that is basically a media downloader for every platformm and is gonna be very usefull.

Requirements:

-Python 3
-Wifi Connection
-Not so much IT Skill

Real Requirements:
- customtkinter
- tkinter
- pytube
- youtube_dl
- instaloader
- tiktokapi
- spotdl
- ffmpeg

(for install this library you have to make this command on you terminal)

Windows:
  py -m pip install <library>

Linux:
  pip install <library>

after you install every library if you aren't Windows User, you have to change this part of the code that's on top, from this:

#REMOVE THE # FROM YOUR OPERATING SYSTEM:
operating_system = 'Windows'
#operating_system = 'Other' #Linux/MacOS

to this:

#REMOVE THE # FROM YOUR OPERATING SYSTEM:
#operating_system = 'Windows'
operating_system = 'Other' #Linux/MacOS

(just change the #)

(this is only necessary if you want to download music from spotify)

AFTER THAT YOU ARE READY TO GO

USAGE:

Windows:

  py main.py
  (make sure you are in the same directory of the file)

Linux:
  python3 main.py


KNOWN ISSUES

- Status bar works only for YT video/audio download, not fot the other
- The GUI is ugly ASF
- Probabbly i can make only a button without the menu for downloading youtube video and so make it more minimal
- sometimes te debug print on the app doesn't display, but it works!
- in download_IG function it doesn't work the download of the video or picture, just the PFP
- downloading from tiktok doesn't work


If you need help or question contact me on Instagram (luca_cosini_2002) or Telegram (Luke133)
