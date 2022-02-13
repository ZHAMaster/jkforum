# 提供 [J_K_F](https://www.jkforum.net/forum-234-1.html "此網址請三思後打開") 網域內的目標網址執行圖片爬蟲

朋友因素，突然想爬蟲這個網頁[X18](https://www.jkforum.net/thread-14377630-1-1.html "請三思後再打開此網址")。  
在此留下CODE紀錄。  

## 執行注意！
  * 下載的照片將存放於網頁同名資料夾當中，  
  * 資料夾位置與執行檔同個地方。

  * 如要使用python執行 先行安裝 beautifulsoup4 (pip3 install beautifulsoup4)
  * 使用py執行，若有類似can't find lxml 的錯誤
      * 請將```
            soup = BeautifulSoup(response.text, 'lxml')
            ```
      * 改成```
            soup = BeautifulSoup(response.text)
            ```
  
## ipynb 程式碼檢視
  <https://github.com/ZHAMaster/jkforum/blob/main/jkforum.ipynb>

## py 程式碼檢視
  <https://github.com/ZHAMaster/jkforum/blob/main/jkforum.py>

## 下載exe執行檔
  如果需要，直接從這邊下載。  
  <https://github.com/ZHAMaster/jkforum/raw/main/jkforum.exe>
