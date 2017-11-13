#! python3
# coding:utf-8
import urllib.request
import urllib
import re
import os
import shutil # 高效处理文件的模块
import random
#sys为system的缩写，引入此模块是为了改变默认编码 
import sys
import importlib
import time
importlib.reload(sys)

host = 'http://www.dianping.com'
#自定义UA头部，直接用即可，不用理解细节
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
user_agents=[
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
"Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
]
directory = str('Shenzhen_Spot_Comment') + '\\'
CommentID = int(0) 

if os.path.exists(directory):
    shutil.rmtree(directory)
    os.makedirs(directory)  #删除后再创建对应的关键词目录
    print ('delete existed directory successfully')
else:
    os.makedirs(directory)
    print ('create directory successfully')

url_comment = host + '/shop/'

def GetProxy():
    proxies=[]
    for line in open('proxy.txt'):
        lineline = line.rstrip('\n')
        proxies.append(lineline)
    return random.choice(proxies)
def Install_opener():
    proxy = {'http':GetProxy()}
    #创建ProxyHandler
    proxy_support = urllib.request.ProxyHandler(proxy)
    #创建Opener
    opener = urllib.request.build_opener(proxy_support)#创建Opener
    opener.addheaders = [('User-Agent', user_agent)] 
    urllib.request.install_opener(opener)
def getShopID(ID):
	path_name = str('深圳景点数据') + '\\' + '\\ShopDataInfo_page_16-25' + '.txt'
	file_shop = open(path_name,"r");
	line = file_shop.readlines()
	return ''.join(line[ID-1].split())
def getCommentNum(ID):
	path_name_comment = str('深圳景点数据') + '\\' + '\\CommentDataInfo_page_16-25' + '.txt'
	file_comment_num = open(path_name_comment, "r");
	line_comment = file_comment_num.readlines()
	return ''.join(line_comment[ID-1].split())
def getComment(SpotID,page):
    path_name = directory + '\\CommentInfo_page_16-25_1' + '.txt'
    file = open(path_name, 'a'); #创建文件
    FileName = directory + '\\CommentInfo_page_16-25_2' + '.txt'
    FileName_pictures = directory + '\\CommentInfo_pic_page_16-25' + '.txt'
    print('file open successfully')
    ShopID = getShopID(SpotID)
    view = url_comment + ShopID + '/review_more?pageno=' + str(page)
    print(view)
    success = False
    while not success:
    	try:
    		Install_opener()
    		response = urllib.request.urlopen(view)
    		dc = response.read().decode('utf-8','ingore')
    		Spot_name = re.findall(r'a\stitle="([^\s]+)"\starget', dc, re.S)
    		items_name = re.findall(r'<img\stitle="([^"]+)"\salt=', dc, re.S)
    		items_time = re.findall(r'<span\sclass="time">([^"]+)</span>', dc, re.S)
    		user_comments = re.findall(r'<div\sclass="J_brief-cont">(.*?)</div>', dc, re.S)
    		items_stars = re.findall(r'class="item-rank-rst\sirr-star([^"]+)">', dc, re.S)
    		items_pictures = re.findall(r'<img\ssrc="([^"]+)"', dc, re.S)
    		items_pictures_user = re.findall(r'title="(.*?)"\sclass="thumb"', dc, re.S)
    		items_goods = re.findall(r'<span\sclass="heart-num">(.*?)</span>', dc, re.S)
    		print(len(Spot_name))
    		print(len(user_comments))
    		mink = min(int(len(items_name)), int(len(items_time)))
    		print(len(items_name))
    		if int(len(items_pictures)) != 0:
    			print(items_pictures[0])
    		comments=int(len(items_name))
    		goods=int(len(items_goods))
    		for x in range(goods,comments):
    			items_goods.append('(0)')
    		print(len(items_goods))
    		if int(len(Spot_name)) != 0:
    			success = True
    			print ('Url Comment successfully')
    		sleepNum=random.randint(0,2)
    		time.sleep(sleepNum)
    	except:
    		print ('Url Comment failed')
    		sleepNum=random.randint(0,2)
    		time.sleep(sleepNum)

    global CommentID
    result = ''
    comment = ''
    try:
    	for index in range(0,mink):
    		CommentID += 1
    		p=re.compile('\s+')
    		items_time_t=items_time[index].replace('&nbsp;','')
    		result = str(CommentID) + '  ' + str(SpotID) + '  ' + items_name[index] + '  ' + items_stars[index] + '  ' + items_goods[index] + '  ' + items_time_t + '\n'
    		file.write(result)                                                                      #将结果存入文件
    		CommentsFile=open(FileName, 'a', encoding="utf-8")
    		items_comments_p=re.sub(p,'',user_comments[index])
    		items_comments_t=items_comments_p.replace('<br/>','')
    		items_comments_s=items_comments_t.replace('&nbsp;','')
    		comment = str(CommentID) + '  ' + items_comments_s + '\n'
    		CommentsFile.write(comment)
    		PicFile=open(FileName_pictures,'a', encoding="utf-8")
    		if int(len(items_pictures)) != 0:
    			for k in range(0,int(len(items_pictures))):
    				if  items_name[index] in items_pictures_user[k]:
    					pic = str(CommentID) + '  ' + items_name[index] + '  ' + items_pictures[k] + '\n'
    					PicFile.write(pic)
    	PicFile.close()
    	file.close()
    	CommentsFile.close()
    	sleepNum=random.randint(0,2)
    	time.sleep(sleepNum)
    	print('Comment Complete!')
    except:
    	print('Comment Failed!')
    	sleepNum=random.randint(0,2)
    	time.sleep(sleepNum)

def start_crawl():
    global CommentID
    for x in range(13,31):
    	CommentNum = getCommentNum(x)
    	page = int(CommentNum)//int(20) + 1 + 1
    	for y in range(1,int(page)):
    		getComment(x,y)
    		if CommentID >= 300:
    			break


start_crawl()