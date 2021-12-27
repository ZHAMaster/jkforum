#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
開發版本：1.0
開發日期：2021/12/27
"""


# In[1]:


from bs4 import BeautifulSoup
import requests
import os
import urllib


# In[3]:


# 輸出更新條
def update_bar(title, temp, total):
    print('\r' + '['+title+']:[%s%s] %s(%.2f%%)' % ('█' * int(temp/total*20), ' ' * (20-int(temp/total*20)), str(temp)+'/'+str(total), float(temp/total*100)), end='')
    if temp == total:
        print ('')


# In[9]:


# 網頁連線與處理
url = input("請輸入www.jkforum.net網域內的目標網址：")
# url = "https://www.jkforum.net/thread-14377630-1-1.html?utm_source=Line&utm_medium=txt&utm_campaign=group"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}

try:
    print ("執行網頁資源抓取...")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    print ("執行成功！")
    # 儲存資料夾
    title_name = soup.title.text[:25]
    if not os.path.exists(title_name):
        os.makedirs(title_name)
        print("創建資料夾，" + title_name)

    print ("資料夾位置：", title_name, "。")
    
    ignore_js_op = soup.find_all('ignore_js_op')
    print ("此次總下載圖量應為：", len(ignore_js_op),"。")
    
    print ("=============== 開始執行下載！ ===============")
    # 圖片截取與下載作業
    for i in range(len(ignore_js_op)):
        img_url = ignore_js_op[i].select("img")[0].get('file')
        img = requests.get(img_url)
        img_path = os.path.join(title_name, str(i).zfill(6)+img_url[img_url.rfind(".", ):])
        update_bar("下載階段", i, len(ignore_js_op)-1)
        if not os.path.isfile(img_path):
            with open(img_path, 'wb') as file:
                file.write(img.content)
                file.flush()
            file.close()
    # END !
    print ("=============== 目標執行完畢！ ===============")
    input("按任意鍵離開")

except Exception as e :
    print ("ERROR COD：", e)
    print ("系統判斷當前出現錯誤，若執行多次一樣有錯誤，請提供錯誤資訊 回報給ZHA。")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




