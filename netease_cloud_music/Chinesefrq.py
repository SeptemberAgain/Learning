import jieba
import numpy
import pandas
import re
import sys

txtname = sys.path[0] + "/lyrics.txt"
file = open(txtname, 'r', encoding='utf-8')
# 中文utf-8读写
content = file.read()
p = re.compile(r'\w*', re.L)
newcontent = p.sub('',content)
newcontent = newcontent.replace('.', '')
newcontent = newcontent.replace('作词', '')
newcontent = newcontent.replace('作曲', '')
file.close()
segments = []
# segs = jieba.lcut(content)
segs = jieba.cut(newcontent, cut_all=False)
# 使用精确模式进行分词
for seg in segs:
    if len(seg) > 1:
        segments.append(seg)

segmentDF = pandas.DataFrame({'词组': segments})
# 生成一个DataFrame

out = segmentDF.groupby("词组")["词组"].agg({"计数": numpy.size}).sort_values(['计数'], ascending=False)
# 进行汇总计数并从小往大计数
# print(df.head(100))
out.to_excel('中文词频.xls', sheet_name='sheet1')