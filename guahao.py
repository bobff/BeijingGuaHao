# coding=utf-8
"""
@author: BobFu
@date: 2017-02-09
@desc: 北京市预约挂号系统余号查询脚本
        自动查询指定科室预约时段内是否有号， 有则自动打开预约页面
"""

import urllib.request, re, time, datetime, webbrowser, sys

if __name__ == '__main__':
    url = sys.argv[1]  # 预约挂号科室排版表页面链接 例如： http://www.bjguahao.gov.cn/dpt/appoint/142-200039602.htm
    print('开始查询', url)
    webbrowser.open(url)
    
    while True:
        f = urllib.request.urlopen(url)
        s=f.read().decode()
        res = re.findall('预约<br>剩余:(?P<count>\d+)<.*value="(?P<date>.+)".*>', s)
        if len(res) > 0:
            webbrowser.open(url)
            sys.exit(0)

        print(datetime.datetime.now())

        time.sleep(1)
