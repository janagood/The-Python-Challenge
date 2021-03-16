'''
the python challenge #7
'''
import cv2
import requests
import webbrowser


def webpage_ok(url):
    return requests.get(url).status_code == 200


if __name__ == '__main__':
    image = cv2.imread('pc7.png')
    cv2.imshow('Oxygen challenge', image)
    cv2.waitKey(0)

    height, width, channels = image.shape
    print(f'height: {height}, width: {width}, channels: {channels}')

    for x in range(1, 603, 7):
        (b, g, r) = image[43, x]
        print(f'(b, g, r) for pixel at ({43}, {x}): ({b}, {g}, {r})')

    print()

    line = ''
    for x in range(1, 603, 7):
        (b, g, r) = image[43, x]
        print(f'(b, g, r) for pixel at ({43}, {x}): ({b}, {g}, {r})')
        line += chr(b)

    print()
    print(f'Message from the bar: {line}')
    print()

    answer = ''.join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))

    url1 = 'http://www.pythonchallenge.com/pc/def/'
    url2 = answer
    url3 = '.html'
    url = url1 + url2 + url3
    print(f'Next challenge page: {url}')
    print(f'Status is {webpage_ok(url)}.')

    webbrowser.open(url)
