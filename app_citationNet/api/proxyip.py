import requests
from bs4 import BeautifulSoup
import re


def proxy_spider():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    i = 1
    result = False  # have got a valid proxy
    while not result:
        url = 'http://www.xicidaili.com/wt/' + str(i)
        r = requests.get(url=url, headers=headers)
        html = r.text
        soup = BeautifulSoup(html, "html.parser")
        datas = soup.find_all(name='tr', attrs={'class': re.compile('|[^odd]')})
        for data in datas:
            soup_proxy = BeautifulSoup(str(data), "html.parser")
            proxy_contents = soup_proxy.find_all(name='td')
            ip_org = str(proxy_contents[1].string)
            ip = ip_org
            port = str(proxy_contents[2].string)
            protocol = str(proxy_contents[5].string)
            result = proxy_check(ip, port, protocol)
            if result:
                break
    proxy_all = protocol.lower() + '://' + ip + ':' + port
    return {'protocal': protocol.lower(),
            'ip': ip,
            'port': port,
            'proxy': proxy_all}


def proxy_check(ip, port, protocol):
    proxy_all = protocol.lower() + '://' + ip + ':' + port
    proxy = {
        'http': proxy_all,
        'https': proxy_all,
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    result = False
    try:
        r = requests.get(url='https://www.ip.cn', headers=headers, proxies=proxy, timeout=5)
        ip_available = re.findall(r'IP：<code>([0-9\.]+)</code>', r.text)[0]
        # geo_ip = re.findall(r'GeoIP: ([a-zA-Z, ]+)</p>', r.text)[0]
        # print(geo_ip)
        if ip_available == ip:
            result = True
    except Exception as e:
        pass
    return result


if __name__ == '__main__':
    print(proxy_spider())
