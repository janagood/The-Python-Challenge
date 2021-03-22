'''
the python challenge #4
'''

import pcutils


def create_linked_list(start):
    print('Next nothings:')
    delim = 'and the next nothing is '
    next_nothing = start
    print(f'    nothing = {next_nothing}')
    while True:
        message = pcutils.get_string_from_page('def/',
                                               'linkedlist',
                                               ending='.php?nothing=' + next_nothing)
        if delim not in message:
            print(f'==last message: {message}')
            break
        next_nothing = message.split(delim)[1]
        print(f'    nothing = {next_nothing}')


if __name__ == '__main__':
    pcutils.try_page('def/', 'linkedlist', '.php',
                     caption='Challenge page')

    message = pcutils.get_string_from_page('def/', 'linkedlist',
                                           ending='.php',
                                           start='<body>',
                                           end='<center>',)
    pcutils.print_lines(message.split(pcutils.NEWLINE),
                        'Hint from page source')

    print()

    create_linked_list('12345')

    create_linked_list('8022')

    pcutils.try_page('def/', 'peak', '.html',
                     caption='Next challenge page')
