'''
the python challenge #5
'''

import urllib.request
import pickle
import requests

'''
 playing with pickle:
     dogs_dict1 = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }
     outfile = open('dogs','wb')
     pickle.dump(dogs_dict1,outfile)
     outfile.close()

     infile = open('dogs','rb')
     dogs_dict2 = pickle.load(infile)
     infile.close()
'''

if __name__ == '__main__':
    url = 'http://www.pythonchallenge.com/pc/def/banner.p'
    pickle_data = requests.get(url).text.encode('utf-8')
    outfile = open('pickle', 'wb')
    outfile.write(pickle_data)
    outfile.close()

    infile = open('pickle', 'rb')
    pickle_stuff = pickle.load(infile)
    infile.close()

    print(f'Pickled stuff from {url}:')
    print()
    print(pickle_stuff)

    print(f'Printing banner...')
    print()
    for line in pickle_stuff:
        print(''.join(ch * w for ch, w in line))
