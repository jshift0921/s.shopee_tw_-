import requests
from bs4 import BeautifulSoup

# 抓取蝦皮即時補貨
def shopee_tw():
    url = "https://s.shopee.tw/1LW8nu0as9"  # 蝦皮泡泡瑪特旗艦店
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quantity = soup.find("div", class_="YMlKec fxKbKc").text  # 使用 BeautifulSoup 解析網頁並提取商品數量信息
    return quantity

if __name__ == "__main__":
    Product_quantity = shopee_tw_back_in_stock()
    message = f"不眠劇場毛絨掛件：{Product_quantity}"
    requests.post("https://ntfy.sh/JPopmart",
    data=message.encode(encoding='utf-8'))
