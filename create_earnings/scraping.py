from selenium import webdriver

def open() :
    # 起動時にオプションをつける。（ポート指定により、起動済みのブラウザのドライバーを取得）
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options)

    # ページのタイトルを表示する
    print(driver.title)
    print("========== source ========== ")
    print(driver.page_source)