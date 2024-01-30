import requests
import matplotlib.pyplot as plt

def get_online(appid):
    # 发送请求，获取游戏的在线人数数据
    url = f"https://steamdb.info/api/GetGraph/?type=concurrent_week&appid={appid}"
    response = requests.get(url)
    data = response.json()
    # 提取数据中的时间和人数
    time = data["data"]["x"]
    online = data["data"]["y"]
    # 返回时间和人数的列表
    return time, online

def plot_online(appid, name):
    # 调用函数，获取游戏的在线人数数据
    time, online = get_online(appid)
    # 绘制折线图
    plt.figure(figsize=(10, 6))
    plt.plot(time, online, color="#FF6902")
    plt.xlabel("Time")
    plt.ylabel("Online")
    plt.title(f"{name} Online Players in the Past Week")
    plt.show()

# 指定要分析的游戏的appid和名字
appid = 730 # CS:GO的appid
name = "Counter-Strike: Global Offensive" # CS:GO的名字
# 调用函数，绘制游戏的在线人数曲线图
plot_online(appid, name)
