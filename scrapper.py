import requests
from bs4 import BeautifulSoup

main_url = 'https://apod.nasa.gov/apod/archivepix.html'
base_url = 'https://apod.nasa.gov/apod/'
FOLDER = 'images'
response = requests.get(main_url)
soup = BeautifulSoup(response.text, 'html.parser')
websites = soup.find_all('a')

for link in websites:
    if ".html" in link.get('href'):
        image_url = base_url + link.get('href')
        img_response = requests.get(image_url)
        soup = BeautifulSoup(img_response.text, 'html.parser')
        image = soup.find('img')
        if image != 'None':
            try:
                image_src = base_url + image.get('src')
                image_name = image.get('src').split("/")[2]
                final_image = requests.get(image_src)
                with open(FOLDER+'/'+image_name, "wb") as f:
                    f.write(final_image.content)
                    print('Image downloaded successfully!!!')
            except:
                print('Link does not contain a valid image...')

print('All images downloaded.')