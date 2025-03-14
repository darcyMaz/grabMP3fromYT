from pytubefix import Playlist, YouTube
import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: py grabmp3playlist.py playlist_link destination")
        return
    
    link = sys.argv[1]
    destination = sys.argv[2]
    playlist = Playlist(link.strip())

    for video in playlist.videos:
        # extract only audio
        audio = video.streams.filter(only_audio=True).first()

        # download the file
        out_file = audio.download(output_path=destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # result of success
        print(audio.title + " has been successfully downloaded.")
    

if __name__ == '__main__':
    main()