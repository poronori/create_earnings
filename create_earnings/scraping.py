from selenium import webdriver
from tkinter import messagebox
from .scraping_data import ScrapingData

def open() :
    print('start open')
    # 起動時にオプションをつける。（ポート指定により、起動済みのブラウザのドライバーを取得）
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options)
    
    cur_url = driver.current_url
    print(cur_url)
    if "https://www.google.com/" in cur_url:
        set_melcari_data()
    elif "https://www.yahoo.co.jp" in cur_url:
        set_yahoo_data()
    else :
        messagebox.showwarning("URL不正", "メルカリかヤフーの取引画面を開いてください。")
    
    print('end open')


# メルカリのデータ取得
def set_melcari_data() :
    date = '2023/8/1'
    name = 'なんかの品名'
    price = '1000'
    commission = '100'
    customer = 'テスト 太郎'
    address = '北海道 名古屋市 伏見'
    code = 'a99999999'
    
    scraping = ScrapingData()
    scraping.setScrapingData(date, name, price, commission, customer, address, code)

# ヤフー？のデータ取得
def set_yahoo_data() :
    date = '2023/9/1'
    name = 'ヤフーの品名'
    price = '2000'
    commission = '100'
    customer = 'サンプル 花子'
    address = '東京都 なんとか区 ほげほげ'
    code = 'b123456789'
    
    scraping = ScrapingData()
    scraping.setScrapingData(date, name, price, commission, customer, address, code)