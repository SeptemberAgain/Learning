import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import re
from scipy.misc import imread
from os import path
import random

def random_color_func(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
    h = random.randint(0, 240) # 在此处修改色相
    s = int(130.0 * 255.0 / 255.0) # 在此处修改饱和度
    l = int(100.0 * float(random.randint(40, 140)) / 255.0) # 在此处修改亮度
    return "hsl({}, {}%, {}%)".format(h, s, l)


content = open('lyrics.txt', encoding='utf-8').read()
p = re.compile(r'\w*', re.L)
newcontent = p.sub('', content)
newcontent = newcontent.replace('.', '')
newcontent = newcontent.replace('作词', '')
newcontent = newcontent.replace('作曲', '')
final = jieba.cut(newcontent, cut_all = False)
space_split = " ".join(final)

d = path.dirname(__file__)
# background = imread(path.join(d, "heart.png")) # 可自定义背景图在cloudy内添加mask=background一项
cloudy = WordCloud(background_color="white",#背景颜色
max_words=250,# 词云显示的最大词数,
max_font_size=50, #字体最大值
random_state=30, scale=2,relative_scaling = 0.5,color_func=random_color_func,)
cloudy.font_path= "Consolas+YaHei+hybrid.ttf"
my_wordcloud = cloudy.generate(space_split)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.savefig('wordcloud.png', dpi=1000)
plt.show()
