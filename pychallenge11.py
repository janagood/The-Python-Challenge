'''
the python challenge #11
'''

import cv2
import numpy
import requests
import webbrowser

def try_next(answer):
    url1 = 'http://www.pythonchallenge.com/pc/return/'
    url2 = answer
    url3 = '.html'
    url = url1 + url2 + url3
    print(f'Next challenge page: {url}')
    status = requests.get(url).status_code
    if status == 401:
        status = requests.get(url, auth=('huge', 'file')).status_code
    print(f'Status is {status}.')
    webbrowser.open(url)

if __name__ == '__main__':
    image = cv2.imread('pc11.png')
    height, width, channels = image.shape
    cv2.imshow('Blank canvas: ', image)

    canvas = 255 * numpy.ones((height, width, 3), dtype='uint8')
    for y in range(0, height - 1, 2):
        for x in range(0, width - 1, 2):
            pixel = image[y, x]
            canvas[y // 2, x // 2] = pixel
    cv2.imwrite('evens.png', canvas)
    cv2.imshow('evens', canvas)
    cv2.waitKey(0)

    try_next('evil')
