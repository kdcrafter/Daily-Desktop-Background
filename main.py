import requests
from PIL import Image
from io import BytesIO
from random import randint
import numpy as np
from sklearn.utils import shuffle
from sklearn.cluster import KMeans

from keys import *
from config import *

def get_image():
    image_number = randint(1, MAX_IMAGES)
    response = requests.get('https://api.unsplash.com/search/photos/' +
        '?client_id=' + UNSPLASH_ACCESS_KEY + 
        '&query=desktop-background' +
        '&orientation=landscape' +
        '&page=' + str(image_number) +
        '&per_page=1')

    if response.status_code != 200:
        print('Status Code:', response.status_code)
        print(response.json()['errors'])
        return
    elif response.json() == {}:
        print('Status Code:', 500)
        print(['Internal Server Error'])
        return

    image_url = response.json()['results'][0]['urls']['raw']
    image_url += ('&q=' + str(COMPRESSION_QUALITY) +
        '&fm=jpg' +
        '&w=' + str(WIDTH) +
        '&h=' + str(HEIGHT) +
        '&fit=min')

    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    
    return image

def color_quantize_image(image):
    # Fit on sample of image
    # TODO: check if this works with black and white images
    print('Fit on sample of image')
    image = np.asarray(image, dtype=np.uint8)
    image_sample = shuffle(image).reshape((WIDTH * HEIGHT, 3))[:IMAGE_SAMPLE_SIZE]
    kmeans = KMeans(n_clusters=NUMBER_COLORS).fit(image_sample)
    clusters = np.around(kmeans.cluster_centers_).astype(np.uint8)

    # Apply cluster colors
    print('Apply cluster colors')
    image = np.apply_along_axis(lambda x: clusters[kmeans.predict([x])[0]], 2, image)
    print(image)
    image = Image.fromarray(image) # TIDO: ensure that image is actually made up of NUMBER_COLORS colors

    return image

if __name__ == '__main__':
    #image = get_image()
    #image.save('temp.jpg')
    image = Image.open('temp.jpg')
    image = color_quantize_image(image)
    image.save('color_quantized_temp.jpg')
