import requests



# join url  :  https://www.douban.com/group/100640/?action=join&ck=bczD

# time : //*[@class="olt"]//tr//*[@class="time"]


UA = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
    "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
    "Mozilla/5.0 (Windows NT 6.3; WO=W64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
    ]
# try:
#     ip = choice(ips)
# except:
#     return False
# else:
#     proxies = {
#         "http": ip,
#     }

headers = {
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language':' zh-CN,zh;q=0.9',
'Cache-Control': 'no-cache',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400',
'X-Requested-With': 'XMLHttpRequest'
}


Proxies = {
  'http': 'http://localhost:8866',
  'https': 'http://localhost:8867',
}
Data = {
    'from': 'zh',
    'to': 'en',
    'query': '经常',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '568832.806193',
    'token': '5d7cb93af2d55ef28fe917990dab3912',
    'domain': 'common'
}







response = requests.post('https://fanyi.baidu.com/v2transapi?from=zh&to=en',data=Data)
response.encoding = 'utf-8'

print(response.text)