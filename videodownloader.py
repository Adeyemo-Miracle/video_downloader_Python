import requests
# print(not 'https://www.youtube.com/watch?v=KAKkwvZ96eU'.endswith('.mp4'))
while True:
    Url = input('Url: ')
    if not Url.lower().startswith(('http://', 'https://')) or not Url.lower().endswith('.mp4'): 
        print('Invalid Video Url. Should include http:// or https://')
    # print('Exiting...')
    # exit(1)
    else:
        print('Valid Url')
        break
filename = 'Video.mp4'
try:
    response = requests.get(Url, stream=True)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
    print(f'Download completed: {filename}')
except Exception as e:
    print(f"A error occurred: {e}")