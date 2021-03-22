'''
this is python challenge #9
'''
import pcutils
import cv2

UN = 'huge'
PW = 'file'


def get_dots(n, s, e):
    captions = ['', 'First dots', 'Second dots']
    dots = pcutils.get_string_from_page(
        'return/', 'good',
        start=s, end=e,
        un='huge', pw='file')
    pcutils.print_lines(dots.split(pcutils.NEWLINE), captions[n])
    dots = list(map(int,
                    ''.join(dots.splitlines()).split(',')))
    print()
    return list(zip(dots[0::2], dots[1::2]))


def connect_the_dots(dots1, dots2):
    canvas = pcutils.create_white_canvas(
        10 + max([y for x, y in dots1]
                 + [y for x, y in dots2]),
        10 + max([x for x, y in dots1]
                 + [x for x, y in dots2]))
    for i in range(1, len(dots1)):
        pt1, pt2 = dots1[i - 1], dots1[i]
        cv2.line(canvas, pt1, pt2, pcutils.BLACK)

    for i in range(1, len(dots2)):
        pt1, pt2 = dots2[i - 1], dots2[i]
        cv2.line(canvas, pt1, pt2, pcutils.RED)

    cv2.imshow('Looks like a cow: ', canvas)
    cv2.waitKey(0)


if __name__ == '__main__':
    pcutils.try_page('return/', 'good', un=UN, pw=PW,
                     caption='Challenge page')
    print()

    connect_the_dots(get_dots(1, 'first:', 'second:'),
                     get_dots(2, 'second:', '-->'))
    print()

    pcutils.try_page('return/', 'cow', un=UN, pw=PW,
                     caption='Cow page')
    message = pcutils.get_string_from_page(
        'return/', 'cow',
        un=UN, pw=PW)
    print(f'Message: {message}')

    pcutils.try_page('return/', 'bull', un=UN, pw=PW,
                     caption='Next challenge page')
