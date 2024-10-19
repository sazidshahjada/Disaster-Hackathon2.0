import yt_dlp

def set_ydl_options(path, custom_name):
    return {
        'format': 'best',
        'outtmpl': f'{path}/{custom_name}.%(ext)s',
        'noplaylist': True
    }

def download_videos(video_info, path):
    try:
        for url, custom_name in video_info.items():
            ydl_opts = set_ydl_options(path, custom_name)
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"Downloading video from: {url} as {custom_name}")
                ydl.download([url])
        print("All downloads completed successfully.")
    except Exception as e:
        print(f"An error occurred while downloading: {e}")

def main():
    video_info = {
        "https://www.youtube.com/watch?v=A06U7mnSwS4": "jamalpur"
    }
    path = "/home/sajid/Work/DISASTER-HACKATHON-2.0/Videos"

    download_videos(video_info, path)

if __name__ == "__main__":
    main()
