import re
import os
import sys
import requests
from selenium import webdriver
from bs4 import BeautifulSoup

chrome_driver = r"E:\CodePractice\Environment\python27\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)

reload(sys)
sys.setdefaultencoding("utf-8")

findImgsrc = re.compile('r<img id="manga".*src=".*?">')

url = 'http://www.guoman8.cc/31308/08.html?p='

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}


def askhtml(url):
    browser = webdriver.Chrome()
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def getdata(soup, j):
    img_list = soup.find_all('img')
    img = img_list[0]
    img = str(img)
    src = re.findall('src="(.*?)"', img)
    if (src == 'http://pic.w1fl.com/images/comic/72/142122/'
               '1608748526fpm5ldyPIjkvziDv.jpg'):
        return 0
    title = soup.find_all('h1')
    titles = soup.find_all('h2')
    title = str(title)
    titles = str(titles)
    title = title[23:-10]
    titles = titles[5:-6]
    title = title.decode('unicode_escape')
    titles = titles.decode('unicode_escape')
    if not os.path.exists('./' + title + '/'):
        os.mkdir('./' + title + '/')
    if not os.path.exists('./' + title + '/' + titles + '/'):
        os.mkdir('./' + title + '/' + titles + '/')
    try:
        with open('./' + title + '/' + titles + '/' + str(j) + '.png', 'wb') as f:
            image = requests.get(src[0], headers=headers).content
            f.write(image)
            print ('Successful!', str(j))
    except Exception as e:
        print(repr(e))


if __name__ == '__main__':
    j = 0
    for i in range(1, 20):
        urls = url + str(i)
        soup = askhtml(urls)
        z = getdata(soup, j)
        if (z == 0):
            break
        j += 1
