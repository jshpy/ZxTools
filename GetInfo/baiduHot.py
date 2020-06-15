#!//usr/bin/env python3
import requests
import re
import json
import os
from lxml import etree

OUTPUT = '.'

headers = {
    'Host': 'top.baidu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}



def getTree(url, headers):
    html = requests.get(url, headers=headers)
    html = etree.HTML(html.content.decode('gbk'))
    return html


def getRank(tree):

    result = tree.xpath('//a[@class="list-title"]/text()')
    cont = ''
    for title in result[:10]:
        cont = cont + '{} \n'.format(title)
    return cont



if __name__ == "__main__":
    res = getRank(getTree('http://top.baidu.com/buzz?b=1&fr=topnews', headers))

    with open(os.path.join(OUTPUT, '百度热搜 Top10'), 'w') as fp:
        fp.write(res)
