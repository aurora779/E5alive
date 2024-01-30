import requests
import re

def get_posts(url):
    # 发送请求，获取网页源码
    response = requests.get(url)
    html = response.text
    # 使用正则表达式匹配帖子标题和链接
    pattern = re.compile(r'<a rel="noreferrer" href="(/p/\d+)" title="(.*?)" target="_blank" class="j_th_tit ">')
    results = pattern.findall(html)
    # 遍历结果，打印标题和链接
    for result in results:
        link = "https://tieba.baidu.com" + result[0]
        title = result[1]
        print(title, link)

# 指定要爬取的吧名和页数
ba_name = "python"
page_num = 1
# 构造目标网址
url = f"https://tieba.baidu.com/f?kw={ba_name}&pn={(page_num-1)*50}"
# 调用函数，获取帖子内容
get_posts(url)
