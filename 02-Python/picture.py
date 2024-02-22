import requests

response = requests.get('https://source.unsplash.com/featured/?猪猪猪')
with open('image.jpg', 'wb') as f:
    f.write(response.content)
