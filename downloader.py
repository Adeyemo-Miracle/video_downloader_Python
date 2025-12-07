import requests
Url = input('Url: ')
if not Url.startswith('http://') and not Url.startswith('https://'): 
    print('Invalid URL. Please include http:// or https://')
    exit(1)
filename = input('Filename: ')
response = requests.get(Url, stream=True)
with open(filename, 'wb') as file:
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            file.write(chunk)
print(f'Download completed: {filename}')