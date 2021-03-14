'''
the python challenge #6
'''

import zipfile
import requests
import webbrowser


def webpage_ok(url):
    # OK status code is 200
    # Not found is 404 (and there are many other codes...)
    return requests.get(url).status_code == 200


if __name__ == '__main__':
    archive = zipfile.ZipFile('channel.zip', 'r')
    print(f'Archive directory:')
    archive.printdir()

    print()

    print(f'readme.txt: ')
    print()
    readme = archive.read('readme.txt').decode('ascii')
    print(f'{readme}')

    print()

    linked_list = dict()
    for txtfile in archive.namelist():
        key = txtfile[0:-4]
        contents = archive.read(txtfile).decode('ascii')
        if 'Next nothing is ' in contents:
            next_key = contents.split('Next nothing is ')[1]
        else:
            next_key = None
        linked_list[key] = [next_key, contents]

    print()

    print(f'Linked list:')
    key = '90052'
    while key is not None:
        next_key, message = linked_list[key]
        print(f'key={key}: next={next_key} message={message}')
        key = next_key

    print()

    print(f'Collecting comments...')
    key = '90052'
    answer = ''
    while key is not None:
        next_key = linked_list[key][0]
        comment = archive.getinfo(key + '.txt').comment.decode('ascii')
        answer += comment
        key = next_key

    print()

    print(f'Voila!')
    print(answer)

    url1 = 'http://www.pythonchallenge.com/pc/def/'
    url2 = 'hockey'
    url3 = '.html'
    url = url1 + url2 + url3
    print(f'Next (not quite) challenge: {url}')
    print(f'Status is {webpage_ok(url)}.')
    webbrowser.open(url)

    url1 = 'http://www.pythonchallenge.com/pc/def/'
    url2 = 'oxygen'
    url3 = '.html'
    url = url1 + url2 + url3
    print(f'Next challenge: {url}')
    print(f'Status is {webpage_ok(url)}.')
    webbrowser.open(url)
