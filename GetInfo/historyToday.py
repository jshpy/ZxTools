#!//usr/bin/env python3
import requests
import re
import json
import time
import os
from lxml import etree

OUTPUT = '.'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}



def getTree(url, headers):
    html = requests.get(url, headers=headers)

    html = etree.HTML(html.content.decode('gbk'))
    return html


def getRank(tree):

    result1 = tree.xpath('//div[@class="cdiv"]/p[1]/a[1]/text()')
    result2 = tree.xpath('//div[@class="cdiv"]/p[1]/a[2]/text()')
    result3 = tree.xpath('//div[@class="cdiv"]/p[1]/a[3]/text()')

    cont = ''
    for i in range(len(result1)):
        cont = cont + '{} {} {} \n'.format(result1[i], result2[i], result3[i])
    return cont



if __name__ == "__main__":
    now = int(time.time())
    timeArray = time.localtime(now)
    res = getRank(getTree('https://today.supfree.net/sheshou.asp?{}'.format(time.strftime("m=%m&d=%d", timeArray)), headers))
    with open(os.path.join(OUTPUT, '历史上的今天'), 'w') as fp:
        fp.write(res)
