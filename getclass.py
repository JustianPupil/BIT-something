# -*- coding:utf-8 -*-

import requests
import time
import sys

cookie = "JSESSIONID=" + str(sys.argv[2])
select = ['ggxxkxkOper', 'tykxkOper']
url = 'http://jwms.bit.edu.cn/jsxsd/xsxkkc/ggxxkxkOper?jx0404id=201720182001412&xkzy=&trjf='

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'http://jwms.bit.edu.cn/jsxsd/xsxkkc/comeInGgxxkxk',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cookie }

k = 1
while True:
    try:
        print(u"第" + str(k) + u"次抢课")
        k = k + 1
        i = 0
        time.sleep(1)
        while i < len(sys.argv) - 3:
            url = 'http://jwms.bit.edu.cn/jsxsd/xsxkkc/' + select[int(sys.argv[1]) - 1] + '?jx0404id=' + str(sys.argv[i + 3]) + '&xkzy=&trjf='
            res = requests.get(url = url, headers = header)
            print(res.content.decode("utf-8"))
            i = i + 1
            if 'true' in res.content:
                exit(0)
    except:
        continue
