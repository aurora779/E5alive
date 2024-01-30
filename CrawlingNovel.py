from bs4 import BeautifulSoup
import requests

def get_chapters(url):
    # 发送请求，获取网页源码
    response = requests.get(url)
    html = response.text
    # 创建BeautifulSoup对象，解析网页
    soup = BeautifulSoup(html, "html.parser")
    # 获取小说名字
    novel_name = soup.find("h1").text
    # 获取小说章节列表
    chapters = soup.find_all("dd")
    # 遍历章节列表，获取章节标题和链接
    for chapter in chapters:
        title = chapter.a.text
        link = "https://www.biquge.com.cn" + chapter.a["href"]
        # 调用函数，获取章节内容
        get_content(novel_name, title, link)

def get_content(novel_name, title, url):
    # 发送请求，获取网页源码
    response = requests.get(url)
    html = response.text
    # 创建BeautifulSoup对象，解析网页
    soup = BeautifulSoup(html, "html.parser")
    # 获取章节内容
    content = soup.find("div", id="content").text
    # 打印小说名字，章节标题和内容
    print(novel_name, title)
    print(content)

# 指定要爬取的小说网址
url = "https://www.biquge.com.cn/book/4772/"
# 调用函数，获取小说章节
get_chapters(url)
