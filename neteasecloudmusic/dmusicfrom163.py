# coding: utf-8
from Crypto.Cipher import AES
import base64
import requests
import sys
from bs4 import BeautifulSoup
import re

headers = {
    'Cookie': 'appver=1.5.0.75771;',
    'Referer': 'http://music.163.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}


second_param = "010001"
third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
forth_param = "0CoJUm6Qyw8W8jud"


def get_params():
    iv = b"0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(bytes.decode(h_encText), second_key, iv)
    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey


def AES_encrypt(text, key, iv):
    pad = 16 - len(text) % 16
    text = text+ pad * chr(pad)
    encryptor = AES.new(bytes(key, encoding = "utf-8"), AES.MODE_CBC, iv)
    encrypt_text = encryptor.encrypt(bytes(text, encoding = "utf-8"))
    encrypt_text = base64.b64encode(encrypt_text)
    return encrypt_text


def get_json(url, params, encSecKey):
    data = {
        "params": params,
        "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data).json()
    return response['data']


music_id = input('请输入歌曲ID：')
first_param = "{\"ids\":\"[%d]\",\"br\":320000,\"csrf_token\":\"\"}" % int(music_id)

url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='
params = get_params()
encSecKey = get_encSecKey()
"""
rsp:{
    [{'url': 'http://m10.music.126.net/20180625040613/03f123b93c136a15ee41ab6b06d880f8/ymusic/
    d6bf/2981/298b/25c600828a44b8b27e140687612b06ba.mp3', 'uf': None, 'id': 229072, 'br': 128000,
     'canExtend': False, 'expi': 1200, 'type': 'mp3', 'fee': 8, 
     'md5': '25c600828a44b8b27e140687612b06ba', 'size': 1836974, 'payed': 0, 'code': 200, 
     'flag': 4, 'gain': -1.02}]}
"""
rsp = get_json(url, params, encSecKey)
music_url = rsp[0].get('url')

nameurl = 'http://music.163.com/song?id='+ str(music_id)
s = requests.session()
s = BeautifulSoup(s.get(nameurl,headers = headers).content,"lxml")
name = re.findall(r'<title>(.+?) -',str(s.find('title')))
if music_url:
    music = requests.get(music_url)
    name = sys.path[0] + "/%s.mp3" % name[0]
    with open(name, "wb") as code:
        code.write(music.content)
    print("下载成功")