import requests
from lxml import etree

'''
url = 'http://172.16.16.11'


def fetch_page(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
    return response


response = fetch_page(url)
page = response.content
html = etree.HTML(page)

xpath_offer1 = '//*[@id="wrap"]/div/div/div[2]/div[9]/div[1]/div[1]/p[1]'
xpath_offer2 = '//*[@id="wrap"]/div/div/div[2]/div[9]/div[1]/div[2]/p[1]'

pages1 = html.xpath(xpath_offer1)
for p in pages1:
    print(p)
'''




# r = requests.get('https://www.douban.com')
#
# print(r.status_code)
#
# print(r.text)
# print(r.encoding)
# print(r.apparent_encoding)
# print(r.raise_for_status())

# r.encoding = 'utf-8'
# print(r.text)


## 通用代码框架
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'

if __name__ == "__main__":
    url = 'https://www.baidu.com'
    print(getHTMLText(url))


