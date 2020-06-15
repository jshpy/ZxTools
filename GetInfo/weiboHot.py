#!//usr/bin/env python3
import requests
import re
import json
import os
from lxml import etree

OUTPUT = '.'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}



def getTree(url, headers):
    html = requests.get(url, headers=headers)
    html = etree.HTML(html.content.decode('utf-8'))
    return html


def getRank(tree):

    result = tree.xpath('//*[@id="pl_top_realtimehot"]/table/tbody/tr/td/a/text()')
    cont = ''
    for title in result[1:11]:
        cont = cont + '{} \n'.format(title)
    return cont

if __name__ == "__main__":
    res = getRank(getTree('https://s.weibo.com/top/summary?Refer=top_hot&topnav=1&wvr=6', headers))

    with open(os.path.join(OUTPUT, '微博热搜 Top10'), 'w') as fp:
        fp.write(res)
