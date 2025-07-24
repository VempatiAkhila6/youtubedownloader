import customtkinter as ctk
from tkinter import ttk
import yt_dlp
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

def download_video():
    url = entry_url.get()
    resolution = resolution_var.get()

    progress_label.pack(pady=(10, 5))
    progress_bar.pack(pady=(10, 5))
    status_label.pack(pady=(10, 5))

    try:
        
        options = {
            'format': f'bestvideo[height<={resolution}]+bestaudio/best', 
            'outtmpl': '%(title)s.%(ext)s',  
            'noplaylist': True,  
            'ffmpeg_location': r'C:\Users\22eg1\OneDrive\Desktop\youtube\ffmpeg.exe',  
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],                                                                  
        }

       
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        status_label.configure(text="Downloaded", text_color="white", fg_color="green")

    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}", text_color="white", fg_color="red")
        print(f"Error: {str(e)}")

root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root.title("YOUTUBE DOWNLOADER")
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=10, pady=10)

url_label = ctk.CTkLabel(content_frame, text="ENTER THE YOUTUBE URL HERE:")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=(10, 5))
entry_url.pack(pady=(10, 5))

download_button = ctk.CTkButton(content_frame, text="Download", command=download_video)
download_button.pack(pady=(10, 5))

resolutions = ["720p", "360p", "240p"]
resolution_var = ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolutions, textvariable=resolution_var)
resolution_combobox.pack(pady=(10, 5))
resolution_combobox.set("720p")

progress_label = ctk.CTkLabel(content_frame, text="0%")
progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0.6)

status_label = ctk.CTkLabel(content_frame, text="Downloaded")

root.mainloop()
