import yt_dlp

class YoutubeConvert:
    def __init__(self, song, artist):
        self.song = song
        self.artist = artist

    def download_song(self):
        # Format the search query
        query = f"{self.song} {self.artist}"
        
        # Set options for yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',  # or 'wav', 'aac', etc.
                'preferredquality': '192',
            }],
            'outtmpl': '%(title)s.%(ext)s',  # Output file name
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Search and download the song
            ydl.download([f"ytsearch:{query}"])

if __name__ == "__main__":
    song = "Bound"
    artist = "Ponderosa Twins Plus One"
    file = YoutubeConvert(song, artist)
    file.download_song()