from aip import AipSpeech
import datetime 
def shibie():
    APP_ID = '15858603'
    API_KEY = 'EdUjl8Xu5cDcaDIp9fzl4EZn'
    SECRET_KEY = 'X3ZECRub139ucxElGbVBtxmiDDcfyPXx'
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    file_handle = open('F:\\音频\\5.wav', 'rb')  
    file_content = file_handle.read()  
    result=client.asr(file_content, 'pcm', 16000, {
        'dev_pid': '1536',
    })
    if result['err_no'] == 0:  
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " >> " + result['result'][0]) 
    else:  
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " >> " + "err_no:" + str(result['err_no'])) 
    return result['result'][0]
