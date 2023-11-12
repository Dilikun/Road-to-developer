from pytube import YouTube

try:
    # ask the user to input the YouTube URL
    url = input('Enter the YouTube URL: ')
    yt = YouTube(url)

    print('Title:', yt.title)
    print('Views: ', yt.views)

    # get the highest resolution stream
    yd = yt.streams.get_highest_resolution()

    # download the video
    yd.download()

    print('Download complete')
except Exception as ex:
    print('An error occurred', str(ex))
