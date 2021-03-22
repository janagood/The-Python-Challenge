'''
the python challenge #7
'''
import pcutils
import os


def get_image_info(image_file_name):
    page_image = pcutils.get_image('def/', 'oxygen', '.png',
                                   caption='Oxygen.png',
                                   filename=image_file_name)

    height, width, channels = page_image.shape
    print(f'image shape: height={height}, width={width}, channels={channels}')

    print()

    print(f'Gray bar pixels (line 43):')
    result = ''
    for x in range(1, 604, 7):
        (b, g, r) = page_image[43, x]
        print(f'(b, g, r) pixel at x={x}: ({b}, {g}, {r})')
        result += chr(b)
    print()
    return result


def get_message(s):
    lines = s.split('. ')
    pcutils.print_lines(lines, 'Message from the bar')
    print()
    message = list(map(int, lines[1].split('[')[1][0:-1].split(', ')))
    return ''.join(map(chr, message))


if __name__ == '__main__':
    pcutils.try_page('def/', 'oxygen', caption='Challenge page')

    answer = get_message(get_image_info('oxygen'))

    pcutils.try_page('def/', answer, caption='Next challenge page')

    os.remove('oxygen.png')
