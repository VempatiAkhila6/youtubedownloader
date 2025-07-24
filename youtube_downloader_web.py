import streamlit as st
import yt_dlp
import os
import ssl

# Disable SSL verification (same as your original code)
ssl._create_default_https_context = ssl._create_unverified_context

# Page configuration
st.set_page_config(
    page_title="YouTube Downloader",
    page_icon="🎥",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #FF0000;
        margin-bottom: 2rem;
    }
    .download-section {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎥 YouTube Downloader</h1>', unsafe_allow_html=True)

# Main content
with st.container():
    st.markdown('<div class="download-section">', unsafe_allow_html=True)
    
    # URL input
    url = st.text_input(
        "Enter YouTube URL:",
        placeholder="https://www.youtube.com/watch?v=...",
        help="Paste the YouTube video URL here"
    )
    
    # Resolution selection
    col1, col2 = st.columns(2)
    with col1:
        resolution = st.selectbox(
            "Select Quality:",
            ["720p", "360p", "240p"],
            index=0,
            help="Choose the video quality"
        )
    
    with col2:
        # Extract just the number from resolution (e.g., "720p" -> "720")
        resolution_number = resolution.replace("p", "")
    
    # Download button
    if st.button("🚀 Download Video", type="primary", use_container_width=True):
        if url:
            # Show progress
            with st.spinner("Downloading video..."):
                try:
                    # Configure download options
                    options = {
                        'format': f'bestvideo[height<={resolution_number}]+bestaudio/best',
                        'outtmpl': '%(title)s.%(ext)s',
                        'noplaylist': True,
                        'ffmpeg_location': r'C:\Users\22eg1\OneDrive\Desktop\projects\ffmpeg.exe',  # Updated path
                        'postprocessors': [{
                            'key': 'FFmpegVideoConvertor',
                            'preferedformat': 'mp4',
                        }],
                    }
                    
                    # Download the video
                    with yt_dlp.YoutubeDL(options) as ydl:
                        # Get video info first
                        info = ydl.extract_info(url, download=False)
                        video_title = info.get('title', 'Unknown Title')
                        
                        st.info(f"Downloading: {video_title}")
                        
                        # Download the video
                        ydl.download([url])
                    
                    st.success("✅ Download completed successfully!")
                    st.balloons()
                    
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.error("Please check the URL and try again.")
        else:
            st.warning("⚠️ Please enter a YouTube URL first.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Instructions
with st.expander("ℹ️ How to use"):
    st.markdown("""
    1. **Copy the YouTube URL** from your browser
    2. **Paste it** in the input field above
    3. **Select your preferred quality** (720p, 360p, or 240p)
    4. **Click Download** and wait for the video to download
    5. **Find your video** in the same folder as this app
    
    **Note:** The video will be saved as an MP4 file in the current directory.
    """)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit and yt-dlp") 