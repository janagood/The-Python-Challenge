'''
this is python challenge #13
'''
import xmlrpc.client
import requests
import webbrowser

if __name__ == '__main__':
    url1 = 'http://www.pythonchallenge.com/pc/'
    url2 = 'phonebook'
    url3 = '.php'
    url = url1 + url2 + url3
    gfx_data = requests.get(url, auth=('huge', 'file')).content

    sp = xmlrpc.client.ServerProxy(url)
    print(f'xmlrpc.client methods: {sp.system.listMethods()}')
    print(f'phone help:')
    print(sp.system.methodHelp('phone'))
    print(sp.phone('Evil'))
    print(sp.phone('Bert'))
# 555-ITALY -- 555 is what they use in movies and tv as fake prefix

    url1 = 'http://www.pythonchallenge.com/pc/return/'
    url2 = 'italy'
    url3 = '.html'
    url = url1 + url2 + url3
    webbrowser.open(url)