##################### prepare data
import requests 

hack  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = "https://python123.io/ws/demo.html"

r = requests.get(url , headers = hack)
r.status_code


r.encoding = r.apparent_encoding


from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, 'html.parser')






######################  find_all function


####### name (name of tags), back the tag

soup.find_all('a')   # all a tags

soup.find_all(['a','b'])   # all a and b tags

soup.find_all(True)  # all tags

for tag in soup.find_all(True):
    print(tag.name)
    
# 模糊查找（正则表达式）
import re

for tag in soup.find_all(re.compile('b')):
    print(tag.name)

    

############ attr: attributes of tag

soup.find_all('p','course')

soup.find_all('a', id = 'link1')  

soup.find_all(id = re.compile('link'))


############3 String （between tags）

soup.find_all(string = "Basic Python")

soup.find_all(string = re.compile("Python"))




