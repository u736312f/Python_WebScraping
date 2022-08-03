# ライブラリの読み込み
from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep
import shutil
import datetime

# webドライバの起動
driver = webdriver.Chrome("[chromedriverを保存したフォルダ]/chromedriver.exe")

# URLの表示
driver.get('https://tide.gsi.go.jp/main.php?number=05&t1=&t2=_sec30&t3=_def&t4=&dt=_20100101&tt=&ap=true&tm=0&yr=2010&mn=1&dy=1&td=false&tds=-1&tmu=day&tmt=1&e=0&base=1')

# 要素の抽出
elements = driver.find_elements(By.NAME, "download_btn")

# 要素の操作
elements[0].click()
sleep(2)

# ファイルの移動
shutil.move('[ダウンロードフォルダ]/05_20100101_sec30_tp.txt', '[移動したいフォルダ]')

# webドライバの停止
driver.quit()
