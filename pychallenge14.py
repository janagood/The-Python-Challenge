'''
the python challenge #14
'''
import numpy
import cv2
import requests
import webbrowser


def create_blank_image(width, height, bgr_color=(255, 255, 255)):
    image = numpy.zeros((height, width, 3), numpy.uint8)
    if bgr_color is not None:
        image[:] = bgr_color
    return image


def get_wire_png():
    url1 = 'http://www.pythonchallenge.com/pc/return/'
    url2 = 'wire'
    url3 = '.png'
    url = url1 + url2 + url3
    wire_file = open('wire.png', 'wb')
    wire_file.write(requests.get(url, auth=('huge', 'file')).content)
    wire_file.close()


def get_spiral():
    image1 = cv2.imread('wire.png')
    image2 = create_blank_image(100, 100)

    start, y1, x2, y2, sz = 0, 0, 0, 0, 100
    while y1 < 10000:
        for _ in range(0, sz):  # top
            image2[y2, x2] = image1[0, y1]
            x2 += 1
            y1 += 1
        x2 -= 1
        y2 += 1
        for _ in range(0, sz - 1):  # right
            image2[y2, x2] = image1[0, y1]
            y2 += 1
            y1 += 1
        x2 -= 1
        y2 -= 1
        for _ in range(0, sz - 1):  # bottom
            image2[y2, x2] = image1[0, y1]
            x2 -= 1
            y1 += 1
        x2 += 1
        y2 -= 1
        for _ in range(0, sz - 2):  # left
            image2[y2, x2] = image1[0, y1]
            y2 -= 1
            y1 += 1
        start += 1
        x2, y2 = start, start
        sz -= 2
    cv2.imwrite('newwire.png', image2)
    cv2.imshow('newwire.png', image2)
    cv2.waitKey(0)


def try_answer(answer):
    url1 = 'http://www.pythonchallenge.com/pc/return/'
    url2 = answer
    url3 = '.html'
    url = url1 + url2 + url3
    webbrowser.open(url)


if __name__ == '__main__':
    get_wire_png()

    get_spiral()

    try_answer('cat')

    try_answer('uzi')
