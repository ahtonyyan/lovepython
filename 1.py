import requests
import bs4

urls = ['www{}.baidu.com'.format(str(i) for i in range(1,300,20))]
print(urls)