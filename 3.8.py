# ライブラリの読み込み
from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep
import shutil
import datetime

# webドライバの起動
driver = webdriver.Chrome("[chromedriverを保存したフォルダ]/chromedriver.exe")

# 開始日時と終了日時の設定
start_date = datetime.date(2010,1,1)
end_date = datetime.date.today()
i_date = start_date

while i_date != end_date:

    # URLの表示
    driver.get('https://tide.gsi.go.jp/main.php?number=05&t1=&t2=_sec30&t3=_def&t4=&dt=_' + str(i_date.year) + str(i_date.month).zfill(2) + str(i_date.day).zfill(2) +'&tt=&ap=true&tm=0&yr=' + str(i_date.year) + '&mn='+ str(i_date.month) +'&dy=' + str(i_date.day) + '&td=false&tds=-1&tmu=day&tmt=1&e=0&base=1')
    sleep(1)
    
    # 要素の抽出
    elements = driver.find_elements(By.NAME, "download_btn")
    
    # 要素の操作
    elements[0].click()
    sleep(2)
    
    # ファイルの移動
    shutil.move('[ダウンロードフォルダ]/05_' + str(i_date.year) + str(i_date.month).zfill(2) + str(i_date.day).zfill(2) + '_sec30_tp.txt', '[移動したいフォルダ]')
    
    i_date = i_date + datetime.timedelta(days=1)
    sleep(1)
    


# webドライバの停止
driver.quit()
