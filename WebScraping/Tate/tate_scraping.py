import requests
import re
import uuid
from bs4 import BeautifulSoup


"""
reference
https://qiita.com/neet-AI/items/98d4194872ee4f53e3b4
"""

save_path = '/Users/kazuki/Documents/DataSet/201221_Tate_Abstraction_1900_2020_Paper/'
img_count = 0
def get_images_in_tate(page_idx):
    response = requests.get("https://www.tate.org.uk/search?cleared=1&q=Abstraction&type=artwork&wdr=1900-2020&wot=4&page=" + str(page_idx))

    try:
        response.raise_for_status() #エラーがでたら止めてくれる
    except Exception as exc:
        print("except{}".format(exc))
        return

    soup = BeautifulSoup(response.text, 'lxml')
    imgs = soup.findAll('img', src=re.compile('^https://www.tate.org.uk/art/images/work/'))
    for img in imgs:

        img_origin = img['src'].split('_')[0] + '_10.jpg'
        #autor_title = img['alt'].split(", ‘")[0] "名前とるなら結構不規則だからテキストで保存した方がいい"
        print(img_origin)

        r = requests.get(img_origin)

        try:
            r.raise_for_status() #エラーがでたら止めてくれる
        except Exception as exc:
            print("except{}".format(exc))
            return

        global img_count 
        with open(save_path + "{0:05d}".format(img_count) + str('.jpg'), 'wb') as f: 
            img_count += 1
            f.write(r.content)

for i in range(1, 265, 1): #range(start, stop, step)
    print("next page is {}".format(i))
    get_images_in_tate(i)
    
print("fnish")
