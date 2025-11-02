import requests
from bs4 import BeautifulSoup

# 抓取蝦皮即時補貨
def shopee_tw_back_in_stock():
    url = "https://s.shopee.tw/6pr5M2V17Y"  # 蝦皮泡泡瑪特旗艦店
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quantity = soup.find("div", class_="YMlKec fxKbKc").text  # 使用 BeautifulSoup 解析網頁並提取股價信息
    return quantity

if __name__ == "__main__":
    Product_quantity = shopee_tw_back_in_stock()
    message = f"sp花生惡作劇/發霉小蛋糕耳機包：{stock_price}"
    requests.post("https://ntfy.sh/JPopmart",
    data=message.encode(encoding='utf-8'))
