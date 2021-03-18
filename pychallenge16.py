'''
the python challenge #16
'''
import numpy
import cv2
import requests
import webbrowser

def create_blank_image(height, width, bgr_color=(255, 255, 255)):
    image = numpy.zeros((height, width, 3), numpy.uint8)
    if bgr_color is not None:
        image[:] = bgr_color
    return image

def find_bar(line):
    pink = numpy.array([255, 0, 255])
    pinks = list()
    for i, bgr in enumerate(line):
        if all(bgr == pink):
            pinks.append(i)
    return pinks

def try_answer(answer):
    url1 = 'http://www.pythonchallenge.com/pc/return/'
    url2 = answer
    url3 = '.html'
    url = url1 + url2 + url3
    webbrowser.open(url)


if __name__ == '__main__':
    image1 = cv2.imread('mozart.png')
    height, width, channel = image1.shape
    image2 = create_blank_image(height, 2 * width)

    bars = list()
    for y in range(0, height):
        pinks = find_bar(image1[y, 0:width])
        bars.append(pinks[0])

    for y, b in zip(range(0, height), bars):
        if b <= width:
            delta = width - b
        else:
            delta = b - width
        image2[y, delta:delta + width] = image1[y, 0:width]
    cv2.imwrite('linedup.png', image2)
    cv2.imshow('lined up', image2)
    cv2.waitKey(0)

    try_answer('romance')