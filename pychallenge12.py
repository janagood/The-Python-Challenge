'''
the python challenge #12
'''

import cv2
import requests

if __name__ == '__main__':
    url1 = 'http://www.pythonchallenge.com/pc/return/'
    url2 = 'evil2'
    url3 = '.gfx'
    url = url1 + url2 + url3
    gfx_data = requests.get(url, auth=('huge', 'file')).content

    # https://www.file-recovery.com/xxx-signature-format.htm
    # jpg header: FF D8 -- FF trailer is FF D9
    # png \211   P   N   G  \r  \n \032 \n
    # GIF8 -- next two are version -- like 9a
    for i in range(0, 5):
        print(f'Header {i}: {gfx_data[i:64:5]}')

    deals = [gfx_data[i::5] for i in range(0, 5)]
    image_formats = ['jpg', 'png', 'gif', 'png', 'jpg']
    for i in range(0, 5):
        file_name = f'deal{str(i)}.{image_formats[i]}'
        deal = open(file_name, 'wb')
        deal.write(deals[i])
        deal.close()
        image = cv2.imread(file_name)
        cv2.imshow(file_name, image)
    cv2.waitKey(0)
