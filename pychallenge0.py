'''
the python challenge 0

'''

import requests
import webbrowser

def webpage_ok(url):
# OK status code is 200
# Not found is 404 (and there are many other codes...)
    return requests.get(url).status_code == 200

if __name__ == '__main__':
    url1 = 'http://www.pythonchallenge.com/pc/def/'
    url2 = '0'
    url3 = '.html'
    url = url1 + url2 + url3
    print(f'Warm up page: {url}')
    print(f'Status is {webpage_ok(url)}.')

    print()

    url2 = str(pow(2, 38))
    url = url1 + url2 + url3
    print(f'2 ** 38 page: {url}')
    print(f'Status is {webpage_ok(url)}.')

# this will acutally open up the page in browser
    webbrowser.open(url)
