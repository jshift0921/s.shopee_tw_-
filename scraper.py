python
import requests
import time
product_url = "https://s.shopee.tw/1LW8nu0as9"
nfty api_url="https://ntfy.sh/JPopmart",
def check stock():
response requests.get(product_url)
if “庫存補貨”in response.text #假設的庫存補貨標記
notify nfty()
def notify_nfty():
data = {
"message": f"商品補貨了!點擊這裡查看:(product_url)"
} requests.post(nfty_api_url, json-data)
If name "main":
while True:
check stock()
time sleep(3600) #每小時檢查一次
