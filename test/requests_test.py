import requests
from lxml import etree


url = 'https://movie.douban.com/top250'
def fetch_page(url):
    response = requests.get(url, verify=False)
    return response

def parse(url):
    response = fetch_page(url)
    page = response.content
    html = etree.HTML(page)

    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result = []

    for element_movie in html.xpath(xpath_movie):
        result.append(element_movie)

    for p in pages:
        fetch_list.append(url + p.get('href'))

    for url in fetch_list:
        response = fetch_page(url)
        page = response.content
        html = etree.HTML(page)
        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)

    for i, movie in enumerate(result, 1):
        title = movie.find(xpath_title).text
        print(i, title)

def main():
    parse(url)
    
if __name__ == '__main__':
    main()



''' # get e.g.

# url = 'http://172.16.16.11'
# url = 'https://www.douban.com/search'
url = 'http://172.16.16.11:8081/heg_api/airportCity/searchAirPortCity.do'


r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# r = requests.get(url, params={'q': 'python', 'car': '1001'})
# r = requests.get(url)

# print(r.text)
# print(r.encoding)
# print(r.content)
print(r.json())
'''


''' # post e.g.
url = 'http://172.16.16.11:8081/heg_api/flight/getLowPriceCalendar.do'
params = {'to': 'BOM', 'from': 'DEL', 'date': '2019-10-24'}
cs = {'token': '12345', 'status': 'working'}
# r = requests.post(url, json=params) # requests默认使用application/x-www-form-urlencoded对POST数据编码
r = requests.post(url, json=params, cookies=cs, timeout=40)   # json

# print(r.text)
# print(r.headers)
print(r.cookies)
'''

''' 上传文件
>>> upload_files = {'file': open('report.xls', 'rb')}
>>> r = requests.post(url, files=upload_files)
'''





