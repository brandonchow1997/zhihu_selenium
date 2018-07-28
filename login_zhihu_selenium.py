# selenium登录知乎爬取关注的话题
# author:brandonchow1997
# data:2018.7.28

from distributed.asyncio import wait
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from lxml import etree

# 声明浏览器对象初始化
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)


def login():
    url = 'https://www.zhihu.com/signup'
    browser.get(url)
    browser.find_element_by_xpath('//div[@class="SignContainer-switch"]/span').click()
    username = browser.find_element_by_name('username')
    username.clear()
    # 输入用户名
    # 输入用户名
    # 输入用户名自己修改
    username.send_keys('123456')
    password = browser.find_element_by_name('password')
    # 输入密码
    # 输入密码
    # 输入密码自己修改
    password.send_keys('123456')
    browser.find_element_by_xpath('/html/body/div[1]/div/main/div/div/div/div[2]/div[1]/form/button').click()
    # 验证码暂时不管

    # 选取话题，展开更多
def action():
    browser.find_element_by_link_text('话题').click()
    # 暂停三秒
    time.sleep(3)
    browser.find_element_by_link_text('展开更多').click()
    # 暂停三秒
    time.sleep(3)

# 获取话题下的关注的话题标签
def get_topic_data():
    html = browser.page_source
    raw_data = etree.HTML(html)
    processed_data = raw_data.xpath('/html/body/div[3]/div[1]/div/ul/li/a/text()')
    for data in processed_data:
        print(data)

    # 点击标签 杜伦大学
    # 自己修改！！
    browser.find_element_by_link_text('杜伦大学（Durham University）').click()
    time.sleep(1)
    # 点击杜伦大学链接
    browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[2]/a[2]').click()


# 获取杜伦大学精选页面下的数据
def get_durham_data():
    # 切换页面
    time.sleep(2)
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])
    time.sleep(3)
    # 点击“精华”
    browser.find_element_by_link_text('精华').click()
    time.sleep(1)
    # 滚轮至最下
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    # 滚轮至最下
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    # 滚轮至最下
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    # 滚轮至最下
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    # 获取页面数据解析
    durham_html = browser.page_source
    items = etree.HTML(durham_html)
    nodes = items.xpath('//*[@id="TopicMain"]/div[3]/div/div/div')
    for i in range(len(nodes)):
        title = nodes[i].xpath('./div/h2/div/a/text()')
        print(title)
        """short_content = data.find(''),
        agree_num = data.find(''),
        comments_num = data.find('')
        processed_data = {
            '问题标题': title_data,
            '内容概要': short_content,
            '点赞数': agree_num,
            '评论数': comments_num
        }"""


if __name__ == '__main__':
    # 模拟登录知乎
    login()
    time.sleep(3)
    # ------------------
    # 展开更多
    action()
    # ------------------
    # 获取数据
    get_topic_data()
    # ------------------
    # 进行爬取杜伦大学精选问题的操作
    get_durham_data()
    # ------------------
    #关闭浏览器
    browser.close()
