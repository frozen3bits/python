# coding *utf-8*
import urllib.request
import urllib.parse
import json
import time


def postHtml(url,data,header):
    """提交需进行翻译的数据表单，url是有道翻译的地址，data是提交表单数据，
    header是浏览器的一些头信息；函数返回值'非真即假'"""
    try:
        head = header
        data = urllib.parse.urlencode(data).encode('utf-8')#表单数据处理
        response = urllib.request.urlopen(url,data)#发起请求
        toBeJson = response.read().decode('utf-8')#数据解码为'utf-8'（一般不是utf-8,就是gbk）
        afterJson = json.loads(toBeJson)#数据解析成json格式
        return afterJson
    except Exception as e:
        print('get Http Request Error: %s' % e)
        return False


print('Welcome to Youdao Dictionary from chen!')
URL = 'http://fanyi.youdao.com/translatesmartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
HEAD = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
DATA = {'type':'AUTO',
        #'i':target,
        'doctype':'json',
        'xmlVersion':'1.8',
        'keyfrom':'fanyi.web',
        'ue':'UTF-8',
        'action':'FY_BY_CLICKBUTTON',
        'typoResult':'true'}

while True:
    target = input('input:')#输入需要翻译的中文或英文
    if target == 'shutdown':#如果输入字符'shutdown'那么退出翻译函数
        print('Thank you for using the script!')
        break
    else:
        DATA['i'] = target
        html = postHtml(URL, DATA,HEAD)#数据返回为真时，输出翻译结果
        if html:
            try:
                #当有道能翻译出该单词，那么那么返回翻译结果
                print(html['smartResult']['entries'][1])
            except KeyError:
                #当有道不能翻译出该单词（eg:ajdfkla），那么会返回输入单词本身
                print(html['translateResult'][0][0]['tgt'])

time.sleep(2)
