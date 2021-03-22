'''
the python challenge 3
'''
import pcutils
import re

if __name__ == '__main__':
    pcutils.try_page('def/', 'equality', caption='Challenge page')

    print()

    mess_below = pcutils.get_string_from_page('def/', 'equality',
                                              start='<!--',
                                              end='-->')
    pcutils.print_lines(mess_below.split(pcutils.NEWLINE)[0:10],
                        'Mess below from web page')
    print('...')

    print()

    pattern = '[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}'
    matches = re.findall(pattern, mess_below)
    pcutils.print_lines(matches, 'Matches')

    print()

    page = ''.join(s[4] for s in matches)
    pcutils.try_page('def/', page,
                     caption='Trying page in url...')
    message = pcutils.get_string_from_page('def/', page, ).strip()
    print(f'Result: {message}')

    print()

    page = ''.join(s[4] for s in matches)
    pcutils.try_page('def/', page, ending='.php',
                     caption='Next challenge page')
