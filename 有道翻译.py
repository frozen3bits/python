import urllib.request
import urllib.parse
import json


content = input("请输入需要翻译的内容:")
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
head = {}
head['Referer'] = 'http://fanyi.youdao.com'
head['User-Agent'] = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = json
data['xmlVerson'] = 2.1
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data, head)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target = json.loads(html)
print(target)
#print("翻译结果:%s" % (target['smartResult'][0][0]['tgt']))
