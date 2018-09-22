import json
import requests
import re
import urllib
import sys
import lxml
from bs4 import *


url = "http://music.163.com/playlist?id=884497844"#若要修改歌单自行替换最末尾的数字即可
headers = {
'Referer':'http://music.163.com/',
'Host':'music.163.com',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firef',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8', 'ignore')
soup = BeautifulSoup(html, "lxml")
filename = sys.path[0] + "/lyrics.txt"
f = open(filename, 'w', encoding='utf-8')
for item in soup.ul.children:
    song_id = item('a')[0].get("href", None)
    pat = re.compile(r'[0-9].*$')
    sid = re.findall(pat, song_id)[0]
    url = "http://music.163.com/api/song/lyric?"+"id="+str(sid)+"&lv=1&kv=1&tv=-1"
    music_url = 'http://music.163.com/song?id='+str(sid)
    s = requests.session()
    s = BeautifulSoup(s.get(music_url, headers=headers).content, "lxml")
    name = re.findall(r'<title>(.+?) -', str(s.find('title')))
    artist = re.findall(r' - (.+?) - ', str(s.find('title')))
    html = requests.post(url)
    json_obj = html.text
    j = json.loads(json_obj)
    try:
        lyric = j['lrc']['lyric']
    except KeyError:
        lyric = " "
    pat = re.compile(r'\[.*\]')
    lrc = re.sub(pat, "", lyric)
    lrc = lrc.strip()
    f.write(name[0]+'\n')
    f.write(artist[0]+'\n')
    f.write(lrc+'\n\n\n')
f.close()

