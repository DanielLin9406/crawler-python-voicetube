import requests
import csv
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('voicetube.html'), 'lxml')
word_list = []


for ele in soup.select('.show_control'):
    id = ele.get('word_id')
    word = []
    for ele2 in ele.select('td:nth-child(2) a'):
        word.append(ele2.string)
        word.append('')
        word.append('')
        word.append('')

    for ele2 in ele.select('td:nth-child(5) b'):
        word.append(ele2.string)

    for ele2 in soup.find_all('small', word_id=id):
        isHighLight = ele2.select('.highlight')
        isStarIcon = ele2.select('.icon-star')
        if len(isHighLight) > 0:
            sentance = []
            for idx, ele3 in enumerate(ele2.strings):
                if idx <= 2:
                    sentance.append(str(ele3))
                else:
                    word.append("".join(sentance))
                    word.append(str(ele3))
        elif len(isStarIcon) > 0:
            sentance = []
            for idx, ele3 in enumerate(ele2.strings):
                if idx <= 5:
                    sentance.append(str(ele3))
                else:
                    word.append("".join(sentance))
                    word.append(str(ele3))
        else:
            for ele3 in ele2.strings:
                word.append(str(ele3))
    word_list.append(word)

with open('output.csv', 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerows(word_list)
