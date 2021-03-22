'''
the python challenge #8
'''

import pcutils
import bz2

def get_auth():
# this is icky but ran into problems with \\s
    page_bytes = pcutils.get_bytes_from_page('def/', 'integrity',
                                             start='<!--', end='-->', )
    un_pw = page_bytes.split(pcutils.bNEWLINE)
    un_bytes = un_pw[0][5:-1].decode('unicode_escape').encode('raw_unicode_escape')
    pw_bytes = un_pw[1][5:-1].decode('unicode_escape').encode('raw_unicode_escape')
    un = bz2.decompress(un_bytes).decode('ascii')
    pw = bz2.decompress(pw_bytes).decode('ascii')
    return un, pw


if __name__ == '__main__':
#    pcutils.try_page('def/', 'integrity',
#                     caption='Challenge page')

# from url text
    next_page = 'good'
    print(f'Next challenge page is ...return/{next_page}.html.')
    print(f'  It needs a username / password.')

    print()

    un, pw = get_auth()
    print(f'Username: {un}')
    print(f'Password: {pw}')

    print()

    pcutils.try_page('return/', next_page, un=un,
                      pw=pw, caption='Next challenge page')
