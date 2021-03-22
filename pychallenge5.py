'''
the python challenge #5
'''

import pickle
import pcutils
import os

def create_pickle_info():
    pickle_data = pcutils.get_bytes_from_page('def/', 'banner', '.p')
    outfile = open('pickle.dat', 'wb')
    outfile.write(pickle_data)
    outfile.close()

    infile = open('pickle.dat', 'rb')
    pickle_table = pickle.load(infile)
    infile.close()

    os.remove('pickle.dat')
    return pickle_table

if __name__ == '__main__':
    pcutils.try_page('def/', 'peak', caption='Challenge page')

    print()

    pickle_table = create_pickle_info()
    pcutils.print_lines(pickle_table, 'Pickle table')

    print()

    print(f'Printing banner...')
    for line in pickle_table:
        print(''.join(ch * w for ch, w in line))

    pcutils.try_page('def/', 'channel', caption='Next challenge page')
