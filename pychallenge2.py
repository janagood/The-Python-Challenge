'''
the python challenge 2
'''
import pcutils
import collections

if __name__ == '__main__':
    pcutils.try_page('def/', 'ocr', caption='Challenge page')

    print()

    s = pcutils.get_string_from_page('def/', 'ocr',
                                     start='<!--',
                                     end='-->', )
    mess_below = s[s.index('%'):]
    pcutils.print_lines(mess_below.split(pcutils.NEWLINE)[0:10],
                        'Mess below from web page')
    print('...')

    print()

    frequencies = collections.defaultdict(lambda: 0)
    for ch in mess_below:
        if ch.isalnum():
            frequencies[ch] += 1
    pcutils.print_lines(frequencies.items(),
                        'Frequencies of characters in mess')

    print()

    page = ''.join(ch for ch, f in frequencies.items()
                   if f == 1)
    pcutils.try_page('def/', page, caption='Next challenge page')
