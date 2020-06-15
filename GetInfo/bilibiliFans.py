#!//usr/bin/env python3
import requests
import re
import json
import os
from lxml import etree

OUTPUT = '.'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'referer': 'https://space.bilibili.com/97400150'
}

def getContent(url, headers):
    cont = requests.get(url, headers=headers)
    return cont.content.decode('utf-8')

def getFollow(cont):
    li = re.findall(r'{.*}', cont)
    if not li:
        return None
    data = json.loads(li[0])
    res = ''
    res = res + '关注数: {} \n'.format(data['data']['following'])
    res = res + '粉丝数: {} \n'.format(data['data']['follower'])
    return res

def getLike(cont):
    li = re.findall(r'{.*}', cont)
    if not li:
        return None
    data = json.loads(li[0])
    res = ''
    res = res + '获赞数: {} \n'.format(data['data']['likes'])
    return res



if __name__ == "__main__":
    cont = getContent('https://api.bilibili.com/x/relation/stat?vmid=97400150&jsonp=jsonp&callback=__jp3', headers=headers)
    res = getFollow(cont)

    cont = getContent('https://api.bilibili.com/x/space/upstat?mid=97400150&jsonp=jsonp&callback=__jp4', headers=headers)
    res = res + getLike(cont)

    with open(os.path.join(OUTPUT, 'bilibili 数据'), 'w') as fp:
        fp.write(res)
