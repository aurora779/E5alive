import requests
import matplotlib.pyplot as plt

def get_sales(appid):
    # 发送请求，获取游戏的销量数据
    url = f"https://steamspy.com/api.php?request=appdetails&appid={appid}"
    response = requests.get(url)
    data = response.json()
    # 提取数据中的游戏名字和销量
    name = data["name"]
    sales = data["owners"]
    # 返回游戏名字和销量
    return name, sales

def plot_sales(appids):
    # 创建空列表，存储游戏名字和销量
    names = []
    sales = []
    # 遍历appid列表，获取每个游戏的名字和销量
    for appid in appids:
        name, sale = get_sales(appid)
        names.append(name)
        sales.append(sale)
    # 绘制柱状图
    plt.figure(figsize=(10, 6))
    plt.bar(names, sales, color="#FF6902")
    plt.xlabel("Game")
    plt.ylabel("Sales")
    plt.title("Steam Games Sales Comparison")
    plt.show()

# 指定要分析的游戏的appid列表
appids = [730, 570, 578080, 271590, 4000] # CS:GO, Dota 2, PUBG, GTA V, Garry's Mod
# 调用函数，绘制游戏的销量柱状图
plot_sales(appids)
