import requests
from bs4 import BeautifulSoup

def get_products(url):
    # 发送请求，获取网页源码
    response = requests.get(url)
    html = response.text
    # 创建BeautifulSoup对象，解析网页
    soup = BeautifulSoup(html, "html.parser")
    # 获取商品列表
    products = soup.find_all("div", class_="item J_MouserOnverReq")
    # 遍历商品列表，获取商品信息
    for product in products:
        # 获取商品标题
        title = product.find("div", class_="row row-2 title").text.strip()
        # 获取商品价格
        price = product.find("div", class_="price g_price g_price-highlight").text.strip()
        # 获取商品销量
        sales = product.find("div", class_="deal-cnt").text.strip()
        # 获取商品链接
        link = "https:" + product.find("a", class_="J_ClickStat")["href"]
        # 打印商品信息
        print(title, price, sales, link)

# 指定要爬取的网址
url = "https://s.taobao.com/search?q=手机"
# 调用函数，获取商品信息
get_products(url)
