from bs4 import BeautifulSoup
import requests
import os
from datetime import date

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

image_file_path_path = os.path.join(BASE_DIR, 'bing_wall_images')

def get_url():
    url = 'http://bing.com'
    req = requests.get(url)
    data = req.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('script'):
        text = link.text
        if 'g_img={url:' in text:
            imglink = text.split('g_img={url:')[1].split(',')[0].replace("'", "")
            break
    if imglink:
        imglink = url + imglink
    return imglink

def download_image(image_url):
    image_url = image_url.replace('"', '').replace(' ', '')
    ext = image_url.split('.')[-1]
    os.system('mkdir -p '+image_file_path_path)
    filename = str(date.today()) + '.' + ext
    image_file_path = "{dir}/{fname}".format(dir=image_file_path_path, fname=filename)
    cmd = "wget '{url}' -O {image_file_path}".format(url=image_url, image_file_path=image_file_path)
    os.system(cmd)
    
    if os.path.isfile(image_file_path):
        os.unlink(image_file_path)
    os.system(cmd)
    return image_file_path

def main():
    image_url = get_url()
    image_file_path = download_image(image_url)
    os.system('gsettings set org.gnome.desktop.background picture-uri file://'+image_file_path)

if __name__ == '__main__':
    main()
