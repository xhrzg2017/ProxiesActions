import urllib.request
import ssl,os
context = ssl._create_unverified_context()

#1.数据url
url = 'https://hk.xhrzg2017.xyz/clash/proxies?nc=CN&type=vmess,trojan&speed=5'
#2.添加请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}
#3.构建请求对象
request = urllib.request.Request(url, headers=headers)  #使用Request可以加请求头对象
#4.发送请求对象
response = urllib.request.urlopen(request,context=context)
#5.读取数据
data = response.read()
#print(data)
#6.保存到文件中 验证数据
dirs = './subscribe'
if not os.path.exists(dirs):
    os.makedirs(dirs)
with open(dirs+'/clash.txt', 'wb') as f:
    f.write(data)
