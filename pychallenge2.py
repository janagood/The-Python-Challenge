'''
the python challenge 2
'''
import requests
import webbrowser
import collections


def webpage_ok(url):
    # OK status code is 200
    # Not found is 404 (and there are many other codes...)
    return requests.get(url).status_code == 200


if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
    webbrowser.open(url)
    print(f'Source for {url}:')
    print()
    print(requests.get(url).text)

# little kludge to get the text from the page source
    mess_below = requests.get(url).text.strip().split('mess below')[1]
    mess_below = mess_below[mess_below.index('%%'):-3]

    frequencies = collections.defaultdict(lambda: 0)
    for ch in mess_below:
        if ch != '\n':
            frequencies[ch] += 1

    for ch, f in frequencies.items():
        print(f'Frequency of {ch} is {f}')

    print()

    url1 = 'http://www.pythonchallenge.com/pc/def/'
    url2 = ''.join(ch for ch, f in frequencies.items()
                   if f == 1)
    url3 = '.html'
    url = url1 + url2 + url3
    print(f'Next challenge page: {url}')
    print(f'Status is {webpage_ok(url)}.')

    webbrowser.open(url)


