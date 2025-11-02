import requests
from bs4 import BeautifulSoup

# 抓取泡泡瑪特庫存數量
def scrape_tsmc_stock_price():
    url = "https://s.shopee.tw/1LW8nu0as9"  # 台灣蝦皮泡泡瑪特旗艦店網站URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    Stock_quantity = soup.find("div", class_="YMlKec fxKbKc").text  # 使用 BeautifulSoup 解析網頁並提取股價信息
    return Stock_quantity

if __name__ == "__main__":
    stock_price = scrape_tsmc_stock_price()
    message = f"不眠劇場毛絨掛件：{stock_price}"
    requests.post("https://ntfy.sh/JPopmart",
    data=message.encode(encoding='utf-8'))
