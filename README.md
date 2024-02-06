使用Selenium套件開啟Chrome瀏覽器，模擬登入Facebook。使用者需要輸入帳號和密碼。
進入目標Facebook社團的網頁。
自動捲動網頁，將網頁上的文章全部載入，以便後續爬取。
使用BeautifulSoup套件解析網頁HTML，找到包含文章資訊的特定HTML元素。
遍歷每一篇文章，提取作者、內文、圖片網址、留言和讚數等資訊。
將提取的資訊儲存到一個字典中。
將字典轉換為Pandas的DataFrame，以便後續分析和處理。
使用Pandas將DataFrame寫入Excel檔案中。
