'''
the python challenge #15

'''
import calendar
import webbrowser


def try_answer(answer):
    url1 = 'http://www.pythonchallenge.com/pc/return/'
    url2 = 'mozart'
    url3 = '.html'
    url = url1 + url2 + url3
    webbrowser.open(url)


if __name__ == '__main__':
    yyyys = [int('1' + str(i).rjust(2, '0') + '6') if i < 10
             else int('1' + str(i) + '6')
             for i in range(0, 99)]

    leap_years = [yyyy for yyyy in yyyys if calendar.isleap(yyyy)]
    print(f'Leap years 1--6: {leap_years}')

    try_answer('mozart')
