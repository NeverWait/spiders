# -*- coding:utf-8 -*-
# -------------------------------------------
# 第二期：

# urllib.urlopen()
# read()
# info()
# getcode()
# ------------------------------------------
# 第三期
# import chardet
# url = "http://iplaypython.com"
# content = urllib.urlopen(url).read()
# print chardet.detect("中文")
# def code_detect(url):
#     """
#
#     """
#     content = urllib.urlopen(url)
#     result = chardet(content)
#     return restult
# chardet.detect

# ------------------------------------

# 第四期 urllib2  抓取禁止爬虫访问的页面  模仿浏览器访问
# random choice()
# import urllib2
# import random
#
# my_headers = ["Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:41.0) Gecko/20100101 Firefox/41.0",
#               "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0",
#               "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) " \
#               "Chrome/45.0.2454.93 Safari/537.36",
#               "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
#               "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0"
#               "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0",
#               "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.6)Gecko/20091201 Firefox/27.0",
#               ]
#
#
# def read_content(web_url):
#     """
#     功能：返回网站页面的信息
#     输入：要获取的页面url
#     输出：返回页面头部的信息
#     """
#
#     head_random = random.choice(my_headers)
#     header_info = {"User-Agent":head_random,
#                   "GET":web_url,
#                   "Host":"blog.csdn.net",
#                   "Referer":"http:/://blog.csdn.net/"}
#     req = urllib2.Request(web_url)
#     req.add_header("User-Agent",head_random)
#     req.add_header("GET",web_url)
#     req.add_header("Host","blog.csdn.net")
#     req.add_header("Referer","http:/://blog.csdn.net/")
#
#     content = urllib2.urlopen(req)
#     content_read = content.read()
#     content.close()
#     return content_read
# url = "http://blog.csdn.net/lxytsos/"
#
# print read_content(url)

# -------------------------------------------------------------

# 第五期 爬虫图片下载

# import urllib
# # import lxml
# from bs4 import BeautifulSoup
#
#
# def get_content(url):
#     """
#     doc
#     """
#
#     content = urllib.urlopen(url)
#     content_read = content.read()
#     # print content.info()  # 头部信息
#     content.close()
#     return content_read
#
#
# def download_ratio(a, b, c):
#     """
#     @a: 已经下载的数据块05
#     @b: 数据块的大小06
#     @c: 远程文件的大小
#     """
#     ratio = 100.0 * a * b / c
#     if ratio > 100:
#         ratio = 100
#     print '%.2f%%' % ratio
#
#
# def get_image(info):
#     """
#     爬取百度贴吧某个某个帖子上面所有的图片,同时显示下载进度
#     """
#     # soup = BeautifulSoup(info, 'html.parser')
#     soup = BeautifulSoup(info, 'lxml')
#     # soup_str = soup.prettify().replace(u'\xa0', '').encode('gbk')
#     img_all = soup.find_all('img')
#     # print len(img_all)  # 111
#     # print img_all[0]['class']
#     # print img_all[0]['src']
#     for i in range(len(img_all)):
#         print i
#         # print img_all[i]['class'] # <type 'list'>
#         if img_all[i]['class'][0] == 'BDE_Image':
#             urllib.urlretrieve(img_all[i]['src'], "E:\\image\\spider\\" + str(i) + ".jpg", download_ratio)
#
# content_info = get_content("http://tieba.baidu.com/p/4055942891")
#
# get_image(content_info)


# -------------------------------------------------
# 其实爬虫并不难，它的流程就是：
# 1：抓取页面
# 2：获取想要的信息

# 以上几个例子的主要学习内容
#
#  第一 urlretrieve()函数
# >>> help(urllib.urlretrieve)
#  Help on function urlretrieve in module urllib:
#
#  urlretrieve(url, filename=None, reporthook=None, data=None)
#
#  参数 finename 指定了保存本地路径（如果参数未指定，urllib会生成一个临时文件保存数据。）
#  参数 reporthook 是一个回调函数，当连接上服务器、以及相应的数据块传输完毕时会触发该回调，
#  我们可以利用这个回调函数来显示当前的下载进度。
#
#  参数 data 指 post 到服务器的数据，该方法返回一个包含两个元素的(filename, headers)元组，
#  filename 表示保存到本地的路径，header 表示服务器的响应头。

# 第二 chardet
# 这个是函数库，用来判断抓取网页或者一个字符串的编码格式，例如
# content = urllib.urlopen(url)
#     result = chardet(content)
#     return restult  # result即为编码格式

# 第三  抓取禁止爬虫访问的页面  模仿浏览器访问（见第四期）
# 对于禁止爬虫爬取的页面，可以用两种方法（或者只用第一种方法）
# 1、配置一下头信息，伪装成浏览器访问
# 2、伪装IP（这种方法后期再实验）

# ------------------------------------------------------
#  抓取视频
import urllib
# import lxml
from bs4 import BeautifulSoup


def download_ratio(a, b, c):
    """
    @a: 已经下载的数据块05
    @b: 数据块的大小06
    @c: 远程文件的大小
    """
    ratio = 100.0 * a * b / c
    if ratio > 100:
        ratio = 100
    print '%.2f%%' % ratio


def get_video(info):
    """
    爬取百度贴吧某个某个帖子上面所有的图片,同时显示下载进度
    """
    url_info = urllib.urlopen(info).read()
    soup = BeautifulSoup(url_info, 'lxml')
    object_all = soup.findAll(attrs={"id": "player"})
    print object_all
    # if img_all[i]['class'][0] == 'BDE_Image':
    #     urllib.urlretrieve(img_all[i]['src'], "E:\\image\\spider\\" + "111" + ".mp4", download_ratio)

content_info = "http://yuntv.letv.com/bcloud.html?uu=a43e1019aa&vu=5e437eb826"

get_video(content_info)


#  http://yuntv.letv.com/bcloud.html?uu=a43e1019aa&vu=5e437eb826
