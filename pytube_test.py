from pytube import YouTube
while True:
    Url = input('Url: ')
    if Url.startswith('https://www.youtube.com/'):
        print('Valid Youtube Url')
        break
    else:
        print('Invalid URL. Please enter a valid YouTube URL.')
stream = YouTube(Url).streams.get_highest_resolution()
stream.download()
print('Download Completed')