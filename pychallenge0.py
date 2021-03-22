'''
the python challenge 0

'''

import pcutils

if __name__ == '__main__':
    pcutils.try_page('def/', '0', '.html',
                     caption='Warm up page')
    print()
    page = str(pow(2, 38))
    pcutils.try_page('def/', page, '.html',
                     caption='New Challenge page')
