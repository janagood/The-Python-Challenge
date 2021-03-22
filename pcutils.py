'''
the python challenge commonly used things

Notes: Things I'm pretty sure of
    requests can't actually
       open the page in browser

    webbrowser can do this
     but username and password
         must be entered manually

also don't really love any of this code
although it helps make the challenges
code nicer
'''

import requests
import webbrowser
import cv2
import numpy

BASIC_URL = 'http://www.pythonchallenge.com/pc/'
NEWLINE = '\n'
bNEWLINE = b'\n'
SPACE = ' '

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def try_page(subdir, page, ending='.html',
             un=None, pw=None, caption=None):
    url = BASIC_URL + subdir + page + ending
    if caption is not None:
        print(f'{caption}: {url}')
    response = requests.get(url).status_code
    if response == 401:
        if un is None:
            if caption is not None:
                print(f'Web page status is {response}.')
        response = requests.get(url, auth=(un, pw)).status_code
    if response == 200:
        webbrowser.open(url)

def get_string_from_page(subdir, page, ending='.html',
                         start=None, end=None,
                         un=None, pw=None):
    url = BASIC_URL + subdir + page + ending
    if un is None:
        t = requests.get(url).text
    else:
        t = requests.get(url, auth=(un, pw)).text
    if start is None:
        return t
    if t is None:
        return None
    lines = t.split(NEWLINE)
    result = ''
    state = 0
    for line in lines:
        if state == 0:
            if line == start:
                state = 1
        elif state == 1:
            if line == end:
                state = 0
            else:
                result += line + NEWLINE
    if len(result) == 0:
        return None
    return result

def print_lines(lines, title, label=None):
    print(f'{title}:')
    for line in lines:
        if len(line) > 0:
            if label is None:
                print(f'  {line}')
            else:
                print(f'  {label} {line}')

def get_bytes_from_page(subdir, page, ending='.html',
              start=None, end=None,
              un=None, pw=None):
    url = BASIC_URL + subdir + page + ending
    start = start.encode()
    end = end.encode()
    if un is None:
        t = requests.get(url).content
    else:
        t = requests.get(url, auth=(un, pw)).content
    if start is None:
        return t
    if t is None:
        return None
    lines = t.split(bNEWLINE)
    result = b''
    state = 0
    for line in lines:
        if state == 0:
            if line == start:
                state = 1
        elif state == 1:
            if line == end:
                state = 0
            else:
                result += line + bNEWLINE
    if len(result) == 0:
        return None
    return result

def get_image(subdir, page, ending='.jpg',
              un=None, pw=None,
              show=False,
              caption='Image', filename='img'):
    data = get_bytes_from_page(subdir, page, ending)
    ifile = open(filename + ending, 'wb')
    ifile.write(data)
    ifile.close()

    image = cv2.imread(filename + ending)
    if show:
        cv2.imshow(caption, image)
        cv2.waitKey(0)
    return image

def create_white_canvas(height, width):
    #    canvas = 255 * numpy.ones((height, width, 3), dtype='uint8')
    return 255 * numpy.ones((height, width, 3))
