'''
the python challenge 1
'''
import requests
import webbrowser


def webpage_ok(url):
    # OK status code is 200
    # Not found is 404 (and there are many other codes...)
    return requests.get(url).status_code == 200


def shift2(ch):
    if ch == 'y':
        return 'a'
    if ch == 'z':
        return 'b'
    return chr(ord(ch) + 2)


def shift_all(sentences):
    return [''.join(shift2(ch)
                    if 'a' <= ch <= 'z' else ch for ch in sentence)
            for sentence in sentences]


if __name__ == '__main__':
    encoded = ['g fmnc wms bgblr rpylqjyrc gr zw fylb.',
               'rfyrq ufyr amknsrcpq ypc dmp.',
               'bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle.',
               'sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.'
               'lmu ynnjw ml rfc spj.']
    print(f'Message to decode:')
    for _ in encoded:
        print(f'    {_}')

    print()

    print(f'Decoded message:')
    for _ in shift_all(encoded):
        print(f'    {_}')

    url1 = 'http://www.pythonchallenge.com/pc/def/'
    url2 = ''.join(shift2(ch) for ch in 'map')
    url3 = '.html'
    url = url1 + url2 + url3
    print(f'Next challenge page: {url}')
    print(f'Status is {webpage_ok(url)}.')

    webbrowser.open(url)
