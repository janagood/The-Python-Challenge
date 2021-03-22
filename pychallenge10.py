'''
the python challenge #10
'''
import pcutils
import itertools

UN = 'huge'
PW = 'file'


def say(k, g):
    # e.g. n = 111221 --> '3' 1s, '2' 2s, '1' 1 --> 312211
    return str(len(list(g))) + k


def look_and_say(n):
    return ''.join(say(k, g) for k, g in itertools.groupby(n))


def get_answer():
    n = '1'
    answers = [n]
    for i in range(1, 31):
        answers.append(look_and_say(answers[i - 1]))
    print(f'Look and say lengths:')
    for i, n in enumerate(answers):
        print(f'  n = {i} -- length = {len(n)}')
    print()
    return str(len(answers[30]))


if __name__ == '__main__':
    pcutils.try_page('return/', 'bull',
                     un=UN, pw=PW,
                     caption='Next challenge page')
    print()

    page = 'sequence'
    pcutils.try_page('return/', page, ending='.txt',
                     un=UN, pw=PW,
                     caption='Clue')
    message = pcutils.get_string_from_page(
                     'return/', page, ending='.txt',
                     un=UN, pw=PW)
    print(f'Message: {message}')

    pcutils.try_page('return/', get_answer(),
                     un=UN, pw=PW,
                     caption='Next challenge page')
