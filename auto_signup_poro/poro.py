import json
import urllib.request
import urllib
import gzip
import http.cookiejar


# 定义一个方法用于生成请求头信息，处理cookie
def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


# 定义一个方法来解压返回信息
def ungzip(data):
    try:  # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data


# 封装头信息，伪装成浏览器
header = {
    'Connection': 'Keep-Alive',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/66.0.3359.170 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'poro.ws',}

url = 'http://poro.ws/auth/login'
opener = getOpener(header)

id = 'YourUserName'  # 你的用户名
password = 'YourPassword'  # 你的密码
postDict = {
    'email': id,
    'passwd': password,
}

postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data)
data = str(data,encoding="utf-8")
myjson=json.loads(data)     #data必须是字符串类型的
newjson=json.dumps(myjson,ensure_ascii=False)   #正常显示中文
print(newjson)

url = 'http://poro.ws/user/checkin'
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = str(data,encoding="utf-8")
myjson=json.loads(data)     #data必须是字符串类型的
newjson=json.dumps(myjson,ensure_ascii=False)       #正常显示中文
print(newjson)
