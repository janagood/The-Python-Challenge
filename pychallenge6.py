'''
the python challenge #6
'''

import pcutils
import zipfile


def get_zip_archive():
    archive = zipfile.ZipFile('channel.zip', 'r')
    readme = archive.read('readme.txt').decode('ascii')
    pcutils.print_lines(readme.split(pcutils.NEWLINE),
                        'readme')
    return archive


def create_linked_list():
    print('Next nothings:')
    delim = 'Next nothing is '
    linked_list = dict()
    for txtfile in archive.namelist():
        key = txtfile[0:-4]
        contents = archive.read(txtfile).decode('ascii')
        if delim in contents:
            next_key = contents.split(delim)[1]
        else:
            next_key = None
        linked_list[key] = [next_key, contents]
    return linked_list


if __name__ == '__main__':
    pcutils.try_page('def/', 'channel', caption='Challenge page')

    print()

    # there is a download for channel.zip
    # manually put in the project directory

    archive = get_zip_archive()
    print()

    linked_list = create_linked_list()

    print(f'Linked list:')
    key = '90052'
    while key is not None:
        next_key, message = linked_list[key]
        print(f'    key={key}: message={message}')
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

    print(f'Trying hockey.html...')
    pcutils.try_page('def/', 'hockey')
    message = pcutils.get_string_from_page('def/',
                                           'hockey')
    print(f'Message: {message}')

    print(f'Trying oxygen.html')
    pcutils.try_page('def/', 'oxygen', caption='Next challenge page')
