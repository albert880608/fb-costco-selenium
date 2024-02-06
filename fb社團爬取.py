# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 01:48:36 2024

@author: User
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
import pyautogui
# 需要的變數與資料庫
count=0
file_path = "fb_data.xlsx"
data = {'文章': [], '圖片網址': [], '留言': [], '讚數': []}
# 輸入需要的變數資料
username = input('請輸入帳號:')
password = input('請輸入密碼:')
scroll_limit = int(input('請輸入網頁滾動次數:'))
# 設定瀏覽器驅動程式與爬蟲網址
chrome_options = ChromeOptions()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://www.facebook.com/")
# 自動登入
elem = browser.find_element("id", "email")
elem.send_keys(username)
elem = browser.find_element("id", "pass")
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
time.sleep(1)
# 進入目標社團
browser.get("https://www.facebook.com/groups/1260448967306807")
# 破解www.facebook.com要求下列權限
x, y = 500, 500
pyautogui.moveTo(x, y, duration=0.5)
pyautogui.click()
# 自動捲網頁
scroll_count = 0  
while scroll_count < scroll_limit:
    browser.execute_script("window.scrollBy(0, window.innerHeight);")
    time.sleep(0.5)  
    scroll_count += 1
# 捲動完畢後開始爬蟲
html_source = browser.page_source
soup = BeautifulSoup(html_source, "lxml")
box = soup.find_all('div', "x1yztbdb x1n2onr6 xh8yej3 x1ja2u2z")
for Group in box:
    # 爬文章
    author = Group.find('a', 'x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f')
    author1 = author.find('span')
    text = author1.text + '\n'
    article = Group.find('div', 'x1iorvi4 x1pi30zi x1l90r2v x1swvt13')
    if article:
        article1 = article.find('div', 'xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs x126k92a')
        Notice = article.find('span',
                              'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xo1l8bm xzsf02u')
        if article1:
            article2 = article1.find_all('div')
            for i in article2:
                if i.text == '查看更多':
                    continue
                else:
                    text += '\n' + i.text
            data['文章'].append(text)
        elif Notice:
            data['文章'].append(Notice.text)
    else:
        data['文章'].append('沒有文章')
    # 爬圖片網址
    imgcheak = Group.find('a', 'x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x1rg5ohu x1a2a7pz x1ey2m1c xds687c x10l6tqk x17qophe x13vifvy x1pdlv7q')
    imgcheak1 = Group.find('a', 'x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lliihq x1pdlv7q')
    if imgcheak:
        data['圖片網址'].append(imgcheak.get('href'))
    elif imgcheak1:
        data['圖片網址'].append(imgcheak1.get('href'))        
    else:
        data['圖片網址'].append('沒有圖片')
    # 爬留言
    a = Group.find('div', 'x1y1aw1k xn6708d xwib8y2 x1ye3gou')
    if a:
        Message = Group.find_all('div', 'xmjcpbm x1tlxs6b x1g8br2z x1gn5b1j x230xth x9f619 xzsf02u x1rg5ohu xdj266r x11i5rnm xat24cr x1mh8g0r x193iq5w x1mzt3pk x1n2onr6 xeaf4i8 x13faqbe')
        text2 = ''
        for i in Message:
            MessageFrom = i.find('span',
                                 'x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x676frb x1nxh6w3 x1sibtaa x1s688f xzsf02u')
            text1 = MessageFrom.text + '\n'
            comments = i.find('div', 'xdj266r x11i5rnm xat24cr x1mh8g0r x1vvkbs')
            comments1 = comments.find_all('div')
            for i in comments1:
                text1 += '\n' + i.text
            text2 += text1 + '\n' + '-----------' + '\n'
        data['留言'].append(text2)
    else:
        data['留言'].append('沒有留言')
    # 爬讚數
    good = Group.find('span', 'xt0b8zv x2bj2ny xrbpyxo xl423tq')
    if good:
        data['讚數'].append(good.text)
    else:
        data['讚數'].append('0')
# pandas處理數據和寫進excel    
df = pd.DataFrame(data)
writer =pd.ExcelWriter("fb.xlsx", engine='xlsxwriter')
df.to_excel(writer, sheet_name="fb", index=False)
writer.close()
                
                
                
                
                