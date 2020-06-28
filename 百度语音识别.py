from aip import AipSpeech
from pydub import AudioSegment


""" 你的 APPID AK SK """
APP_ID = '15858603'
API_KEY = 'EdUjl8Xu5cDcaDIp9fzl4EZn'
SECRET_KEY = 'X3ZECRub139ucxElGbVBtxmiDDcfyPXx'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
filePath="F:\\音频\\3.mp3"
#将mp3转换为wav
AudioSegment.converter = r"D:\ffmpeg-20190327-681957b-win64-static\bin\ffmpeg.exe"
sound = AudioSegment.from_mp3(filePath).set_frame_rate(16000)
sound.export(filePath, format="wav")
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
result = client.asr(get_file_content(filePath), 'wav', 16000, {
    'dev_pid': 1536,
})
print(result['result'])
