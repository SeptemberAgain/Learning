# encoding = utf-8
import os, xlrd, xlwt, re, time


# 获取某个工作目录下的所有xls文件的全称（排除生成的汇总表）
def file_name(file_dir):
    xlslist = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.xls' and checkContainfinal(os.path.splitext(file)[0]):
                xlslist.append(os.path.join(root, file))
    return xlslist


# 对汇总表的正则匹配
def checkContainfinal(word):
    pattern = re.compile(r'^汇总$')     # 匹配文件名称为“汇总”的字符串
    match = pattern.findall(word)
    if match:
        return False
    else:
        return True


# 对报表名称的正则匹配
def checkContainName(word):
    pattern = re.compile(r'[^_]*_([^_]*)_.*')   # 匹配'_'之间'_'的字符串
    match = pattern.findall(word)
    if match:
        return match[0]
    else:
        return word


# 对结尾括弧序号的匹配
def checkContainduplicate(word):
    pattern = re.compile(r'.*([\(（]{1}[0-9]+[\)）]{1})$')  # 匹配含“（数字）或 (数字)”的字符串
    match = pattern.findall(word)
    if match:
        return match[0]
    else:
        return False

# 对原始字符中括号的匹配
def checkContainbrackets(word):
    word = word.replace('(', '\(')
    word = word.replace(')','\)')
    return word


# 设置字体颜色
def setStyle1(name, height, fontcolor, bold):
    style = xlwt.XFStyle()  # 初始化样式
    alignment = xlwt.Alignment()
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 字体类型：比如宋体、仿宋也可以是汉仪瘦金书繁
    font.colour_index = fontcolor  # 设置字体颜色
    font.height = height    # 字体大小
    font.bold = bold        # 定义格式
    style.font = font
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平居中
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
    style.alignment = alignment
    return style

def setStyle2(name, height, fontcolor, bold):
    style = xlwt.XFStyle()  # 初始化样式
    alignment = xlwt.Alignment()
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 字体类型：比如宋体、仿宋也可以是汉仪瘦金书繁
    font.colour_index = fontcolor  # 设置字体颜色
    font.height = height    # 字体大小
    font.bold = bold        # 定义格式
    style.font = font
    alignment.horz = xlwt.Alignment.HORZ_LEFT  # 水平居左
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
    style.alignment = alignment
    return style


def setStyle3(name, height, fontcolor, bold):
    style = xlwt.XFStyle()  # 初始化样式
    alignment = xlwt.Alignment()
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 字体类型：比如宋体、仿宋也可以是汉仪瘦金书繁
    font.colour_index = fontcolor  # 设置字体颜色
    font.height = height    # 字体大小
    font.bold = bold        # 定义格式
    style.font = font
    alignment.horz = xlwt.Alignment.HORZ_RIGHT # 水平居右
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 垂直居中
    style.alignment = alignment
    return style


def main():
    print('开始提取数据...')
    start = time.clock()
    newfile = xlwt.Workbook()   # 打开新的写文档对象
    newtable = newfile.add_sheet('Sheet1', cell_overwrite_ok=True)  # 所有写数据都在Sheet1内，允许覆盖
    ####################################################################################
    #   请在header[]里面加上第一行表头名称，可任意填写，或者调换位置，但是数量和逻辑关系请务必与下面的matchmethod保持对应
    header = ['内容','实收资本金额/成本','资产类合计/市值','基金资产净值/市值','可分配利润/科目名称','银行存款/市值','清算备付金/市值', \
              '存出保证金/市值','应收利息/市值','应收股利/市值','证券清算款/市值','股票投资/市值', \
              '理财产品/市值','资产支持证券/成本','信托计划/成本','信托计划/市值','债券/成本','债券/市值','持有至到期投资/成本', \
              '持有至到期投资/市值','持有至到期投资_债权/市值','可供出售金融资产/成本','可供出售金融资产/市值','委托贷款/成本', \
              '委托贷款/市值','企业份额/成本','企业份额/市值','理财产品/成本','理财产品/市值','信贷资产/成本','信贷资产/市值', \
              '债权资产/成本','债券资产/市值','正回购/成本','正回购/市值','逆回购（+股质）/成本', \
              '逆回购（+股质）/市值','股票质押式回购/成本','股票质押式回购/市值','净值年增长率(%)/科目名称']
    ####################################################################################
    #   请在matchmethod[]里面加上匹配的项目，字符串形式，以符号/隔开，左边为原始表中行的名称，右边为原始表中列的名称
    matchmethod = ['内容','实收资本金额/成本','资产类合计/市值','基金资产净值/市值','可分配利润/科目名称','银行存款/市值','清算备付金/市值', \
              '存出保证金/市值','应收利息/市值','应收股利/市值','证券清算款/市值','股票投资/市值', \
              '理财产品/市值','资产支持证券/成本','信托计划/成本','信托计划/市值','债券/成本','债券/市值','持有至到期投资/成本', \
              '持有至到期投资/市值','持有至到期投资_债权/市值','可供出售金融资产/成本','可供出售金融资产/市值','委托贷款/成本', \
              '委托贷款/市值','企业份额/成本','企业份额/市值','理财产品/成本','理财产品/市值','信贷资产/成本','信贷资产/市值', \
              '债权资产/成本','债券资产/市值','卖出回购金融资产款/成本','卖出回购金融资产款/市值','买入返售金额资产/成本', \
              '买入返售金额资产/市值','股票质押式回购/成本','股票质押式回购/市值','净值年增长率(%)/科目名称']
    row_match = []
    col_match = []
    for i in  range(1, len(matchmethod)):
        matchmethod[i] = checkContainbrackets(matchmethod[i])
        first_part = re.compile(r'^(.*)/(.*)').findall(matchmethod[i])[0][0]
        second_part = re.compile(r'^(.*)/(.*)').findall(matchmethod[i])[0][1]
        row_match.append(re.compile(r'^(%s).?$'%first_part))
        col_match.append(re.compile(r'^(%s).?$'%second_part))
    style = setStyle1('微软雅黑', 220, 0x08, True)     # 单元格设置：居中，字体为微软雅黑，字号11，黑色，加粗
    for i in range(len(header)):
        newtable.write(0, i, header[i], style)   # 填充第一行
    k = len(file_name(os.getcwd()))     # 计算总共的文档数
    print('运行时间几秒到几十秒不等，休息一下吧')
    style = setStyle3('Arial', 200, 0x08, False)  # 单元格设置：靠右，字体为Arial，字号10，黑色，不加粗
    files = []
    for n in range(k):    # 遍历当前工作目录下所有的xls文件
        name = re.compile(r'\\([^\\]*)\.xls').findall(file_name(os.getcwd())[n])[0]    # 获取报表名称
        if checkContainduplicate(name): # 检查报表名称是否能简写
            _string = checkContainduplicate(name)   # 检查括弧序号
            name = checkContainName(name) + ' ' + _string   # 若有则在尾部添加
        else:
            name = checkContainName(name)
        if name in files:
            name = name + '(2)'
        data = xlrd.open_workbook(file_name(os.getcwd())[n])    # 打开新的读文档对象
        for num in range(0, len(data.sheet_names())):
            files.append(name)
            table = data.sheet_by_name(data.sheet_names()[num])   # 定位到第一个工作簿
            rows = table.nrows      # 记录文档的行数
            cols = table.ncols      # 记录文档的列数
            temp_row = [-1]*len(row_match)
            temp_col = [-1]*len(col_match)
            for i in range(rows):       # 嵌套循环遍历所有元素
                for j in range(cols):
                    for x in  range(0, len(row_match)):
                        if row_match[x].findall(str(table.row_values(i)[j])) and temp_row[x] == -1:
                            temp_row[x] = i
                        if col_match[x].findall(str(table.row_values(i)[j])) and temp_col[x] == -1:
                            temp_col[x] = j

            for i in range(len(temp_row)):
                if temp_row[i] == -1 or temp_col[i] == -1:
                    newtable.write(n+1+num, i+1, '')
                else:
                    newtable.write(n+1+num, i+1, str(table.row_values(temp_row[i])[temp_col[i]]), style)  # 填充n行i列
    style = setStyle2('微软雅黑', 200, 0x08, False)  # 单元格设置：靠左，字体为微软雅黑，字号10，黑色，不加粗
    for i in range (k):
        newtable.write(i+1, 0, files[i], style)  # 填充第n行A列
    newtable.col(0).width = 256 * 40     # 设置第一行的列宽
    for i in range(1, len(header)):
        newtable.col(i).width = 256 * 25     # 设置后面的列宽
    newfile.save('汇总.xls') # 保存文件
    print('---------------------------------------------------------------')
    print('处理完成! 用时: %d 秒' % (time.clock() - start))
    print('一共处理', k, '个报表，汇总文档已保存至 汇总.xls')
    print('---------------------------------------------------------------')
    print('注意：可能存在重复行！建议在Excel里经过全选——数据——删除重复项来确定最终的结果')


if __name__ == '__main__':
    main()
