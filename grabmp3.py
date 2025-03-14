from pytubefix import YouTube
import os

# Code pulled from GeeksForGeeks: https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/
def main():

    # url input from user
    yt = YouTube(
    str(input("Enter the URL of the video you want to download: \n>> ")))

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    destination = str(input(">> ")) or '.'

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")

if __name__ == "__main__":
    main()