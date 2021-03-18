'''
the python challenge #17

'''

import requests
import bz2
import urllib.parse
import xmlrpc.client


def get_cookie_info():
    url1 = 'http://www.pythonchallenge.com/pc/def/'
    url2 = 'linkedlist'
    url3 = '.php'
    url = url1 + url2 + url3
    print(f'Cookie info for {url}:')
    cookie_info = requests.get(url).cookies['info']
    print(f'    {cookie_info}')
    print()


def get_cookies():
    cookies = list()
    print(f'URL cookie info:')
    url1 = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
    url2 = '12345'
    url = url1 + url2
    cookie_info = requests.get(url).cookies['info']
    print(f'url cookie info: {url2} {cookie_info}')
    cookies.append(cookie_info)
    while True:
        try:
            url2 = requests.get(url).text.strip().split('next busynothing is ')[1]
            url = url1 + url2
            cookie_info = requests.get(url).cookies['info']
            print(f'url cookie info: {url2} {cookie_info}')
            cookies.append(cookie_info)
        except:
            no_nothing = requests.get(url).text
            print(f'End of the chain message: {url2} {no_nothing}')
            print()
            return ''.join(cookies)


def get_phone_number(data):
    comp = bz2.BZ2Compressor()
    decomp = bz2.BZ2Decompressor()
    unparsed = cookies_data.replace('+', ' ')
    parsed = urllib.parse.unquote_to_bytes(unparsed)
    print(f'data from urllib.parse: {parsed}')
    print(f'data from bz2.decomp: {bz2.decompress(parsed).decode()}')
    sp = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
    return sp.phone('Leopold')


if __name__ == '__main__':
    get_cookie_info()

    cookies_data = get_cookies()
    print(f'data from cookies: {cookies_data}')

    print()

    print(f'phone number: {get_phone_number(cookies_data)}')

    print()

    url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
    message = 'the flowers are on their way'
    clue = requests.post(url, headers={'Cookie': 'info=' + message}).content.decode()
    print(f'Final clue:')
    print(clue)
