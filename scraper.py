stock_element = soup.select_one('.stock-status') #替換為正確的選擇器

if stock_element:

stock_quantity = stock_element.text.strip()

print(f"庫存數量: {stock_quantity}")

else:

print("未找到庫存信息”)

except Exception as e:

print(f"發生錯誤: {e}")

if name == "main":

url = "https://s.shopee.tw/1LW8nu0as9”#替換為實際商品網址

while True:

check_stock(url)

time.sleep(60) #每分鐘檢查一次
