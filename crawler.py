import requests
import csv
import sys
from bs4 import BeautifulSoup

fileName = sys.argv[1:] or 'Template/VoiceTube.html'
soup = BeautifulSoup(open(fileName), 'lxml')
word_list = []


def getVocabulary(ele):
    result = []
    for ele2 in ele.select('td:nth-child(2) a'):
        result.append(ele2.string)
        result.append('')
        result.append('')
        result.append('')
    return result


def getExplanation(ele):
    result = []
    for ele2 in ele.select('td:nth-child(5) b'):
        result.append(ele2.string)
    return result


def getExampleAndTranslation(id):
    result = []
    for ele2 in soup.find_all('small', word_id=id):
        isHighLight = ele2.select('.highlight')
        isStarIcon = ele2.select('.icon-star')
        if len(isStarIcon) > 0 or len(isHighLight) > 0:
            result.extend(hasStarIconOrHighLight(ele2))
        else:
            result.extend(defaultCase(ele2))
    return result


def hasStarIconOrHighLight(ele2):
    result = []
    sentance = []
    expAndtranslationLen = len(list(enumerate(ele2.strings)))
    for idx, ele3 in enumerate(ele2.strings):
        if idx <= expAndtranslationLen - 2:
            sentance.append(str(ele3))
        else:
            result.append("".join(sentance))
            result.append(str(ele3))
    return result


def defaultCase(ele2):
    result = []
    for ele3 in ele2.strings:
        result.append(str(ele3))
    return result


for ele in soup.select('.show_control'):
    id = ele.get('word_id')
    word = []

    word.extend(getVocabulary(ele))
    word.extend(getExplanation(ele))
    word.extend(getExampleAndTranslation(id))

    word_list.append(word)

with open('output/output.csv', 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerows(word_list)