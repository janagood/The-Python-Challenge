'''
the python challenge #8
'''

import bz2
import requests
import webbrowser


def webpage_ok(url, un_pw):
    return requests.get(url, auth=un_pw).status_code == 200

if __name__ == '__main__':
    un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    print(f'Username: {bz2.decompress(un)}')
    pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
    print(f'Password: {bz2.decompress(pw)}')

    print()

    url1 = 'http://www.pythonchallenge.com/pc/return/'
    url2 = 'good'
    url3 = '.html'
    url = url1 + url2 + url3
    print(f'Next challenge page: {url}')
    un_pw = ('huge', 'file')
    print(f'Status is {webpage_ok(url, un_pw)}.')

    webbrowser.open(url)
