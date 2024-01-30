from selenium import webdriver
import time

def get_movies(url):
    # 创建浏览器对象
    driver = webdriver.Chrome()
    # 打开目标网址
    driver.get(url)
    # 等待页面加载完毕
    time.sleep(3)
    # 获取电影列表
    movies = driver.find_elements_by_xpath('//div[@class="movie-item"]')
    # 遍历电影列表，获取电影信息
    for movie in movies:
        # 获取电影标题
        title = movie.find_element_by_xpath('.//p[@class="name"]/a')
        # 获取电影评分
        score = movie.find_element_by_xpath('.//p[@class="score"]')
        # 打印电影标题和评分
        print(title.text, score.text)
    # 关闭浏览器
    driver.quit()

# 指定要爬取的电影网址
url = "https://maoyan.com/films?showType=3"
# 调用函数，获取电影信息
get_movies(url)
