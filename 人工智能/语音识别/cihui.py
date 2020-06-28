from aip import AipNlp
import json


def cihui(t):
    APP_ID = '15874915'
    API_KEY = 'TeCFWb6YplxI3uzzizSInu2l'
    SECRET_KEY = 'asSiGgkYB2X0d5S5QbgoCUtkC737jxwW'

    client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
    
    text = t.encode('gbk').decode('gbk')
    """ 调用词法分析 """
    result1 = client.lexer(text)
    keyword = ['原理','步枪']
    for i in range(len(result1.get('items'))):
        print(result1.get('items')[i].get('item'),result1.get('items')[i].get('pos'))
    for i in range(len(result1.get('items'))):
        for j in  keyword:
            if((result1.get('items')[i].get('pos') == 'n' or result1.get('items')[i].get('pos') == 'nz') and result1.get('items')[i].get('item') == j):
                print("把子弹夹插入握把的弹匣内，因为弹夹左侧有个凹洞，和弹匣卡榫固定住后，拉动枪管衬套，衬套里是复进弹簧，当拉动枪管衬套后，到达弹夹上方，挂弹，松手后，受到复进弹簧的弹力，把子弹带动到了枪膛。这时子弹已经插入到位，即枪管的进弹口，此时子弹已在枪膛内。在拉动衬套的同时把击锤也张开，再把保险打开，当扣动扳机后，击锤打击撞针，撞针快速撞击子弹壳底火，子弹壳内的发射药燃烧，产生膨胀气体，将子弹头推出去。")
