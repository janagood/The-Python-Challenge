'''
the python challenge 1
'''

import pcutils


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
    pcutils.try_page('def/', 'map', caption='Challenge page')

    print()

    encoded = pcutils.get_string_from_page('def/',
                                           'map',
                                           start='<font color="#f000f0">',
                                           end='</tr></td>')
    pcutils.print_lines(encoded.split('. '),
                        'Message to decode')

    pcutils.print_lines(''.join(shift_all(encoded)).split('. '),
                        'Decoded message')

    page = ''.join(shift2(ch) for ch in 'map')
    print(f'map shifted: {page}')
    pcutils.try_page('def/', page, '.html', caption='Next challenge page')
