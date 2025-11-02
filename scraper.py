import requests
import json
# 你的API密钥和访问令牌
api_key = 'YOUR_API_KEY'
access_token = 'YOUR_ACCESS_TOKEN'
# 库存更新API的URL
inventory_update_url = 'https://s.shopee.tw/1LW8nu0as9'
# 示例：更新商品库存
def update_inventory(item_id, stock_quantity):
headers = {
'Content-Type': 'application/json',
'Authorization': 'Bearer ' + access_token,
'shopid': 'YOUR_SHOP_ID'
}
payload = {
"item_ids": [item_id],
"stocks": [stock_quantity]
}
response = requests.post(inventory_update_url, headers=headers, data=json.dumps(payload))
if response.status_code == 200:
print("库存更新成功")
else:
print("库存更新失败，错误代码：", response.status_code)
print(response.text)
# 调用函数更新库存
update_inventory(123456789, 10) # 假设商品ID为123456789，更新库存为10件
