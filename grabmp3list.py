from pytubefix import YouTube
import os
import sys

# Code pulled from GeeksForGeeks: https://www.geeksforgeeks.org/download-video-in-mp3-format-using-pytube/
def main():

    if len(sys.argv) > 3:
        print("There are too many command line arguments.\nUsage: py grabmp3list || py grabmp3list file_path || py grabmp3list file_path destination_folder")
        return
    if len(sys.argv) == 1:
        file_path = str(input("Enter the file path holding the YouTube links: \n>> "))
        print("Enter the destination (leave blank for current directory)")
        destination = str(input(">> ")) or '.'
    elif len(sys.argv) == 2:
        file_path = sys.argv[1]
        print("Enter the destination (leave blank for current directory)")
        destination = str(input(">> ")) or '.'
    else:
        file_path = sys.argv[1]
        destination = sys.argv[2]


    with open(file_path, 'r') as file:
        for line in file:

            # url input from user
            yt = YouTube(line.strip())

            # extract only audio
            video = yt.streams.filter(only_audio=True).first()

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