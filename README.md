# Learning
Code for food.

[![Python](https://img.shields.io/badge/Python-3.5%2B-blue.svg)](https://www.python.org)

### 使用方法：

1. 安装`Python` (3.5 或更高版本）

2. 下载代码

3. 安装依赖：`pip install -r requirements.txt`（先切换到相应文件夹目录）

4. 运行：`按名称运行各个py文件`
<br>

## No.1 `10_sort_method`
十大经典排序的Python实现
![](https://i.imgur.com/7Oh1lj3.png)


## No.2 `auto_signup_poro`
Poro自动签到获取流量

在`id`处和`password`处修改好自己的用户名密码即可


## No.3 `neteasecloudmusic`
### 网易云音乐的相关爬虫

### 1. `dmusicfrom163.py` 
根据歌曲id名称下载mp3格式的音乐（320K优先），存为`歌曲名.mp3`

![](https://i.imgur.com/YBF9TTF.png)

### 2. `lyric.py`
根据歌单id名称打包下载其中每首歌的歌词（含歌名和歌手名）,存为`lyrics.txt`

![](https://i.imgur.com/Ibc4BNY.png)

### 3. `frequency.py`
词频统计，包含中英文，存为`词频.xls`，排序由高到低

### 4. `Chinesefrq.py`
词频统计，仅包含中文，存为`中文词频.xls`，排序由高到低

### 5. `lyricwordcloud.py`
根据之前的歌词文件制作词云，背景图片，字体及色调均可根据注释做相应的调整
![](https://i.imgur.com/XcLSQ33.png)

## No.4 `pyguitar`
通过Karplus算法模拟吉他拨弦的声音，通过带不同的参数运行，有各种不同的效果：

`python music.py --display`    	依次产生不同基频的声音，并绘制频谱图

`python music.py --play`  		随机播放指定频率的声音，计算机“创作”一首歌曲

`python music.py --piano` 		自定义键盘按键，按下发声，开始你的表演

`python music.py --playasong` 	根据吉他谱，电脑为你弹奏一曲