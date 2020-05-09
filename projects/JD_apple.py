import requests
import re
import bs4

import csv

def getHTML(url):
    hack  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r = requests.get(url, timeout = 30, headers = hack)
    r.encoding = r.apparent_encoding        
    return r.text

def parsePage(goodlist, html):
    soup = BeautifulSoup(html, "html.parser")
    lst = soup.find_all("li", class_='gl-item')
  
    for item in lst:
        name = item.find("div", class_= "p-name p-name-type-2").find("em").text
        p = item.find("div", class_= "p-price").find("i").text
        goodlist.append([name,p])
    
    return goodlist


    
def main():
    goods = "apple"
    depth = 5
    start_url = "https://search.jd.com/Search?keyword=" + goods
    finallist = []   
    # loop for dif pages:
    for i in range(depth):
        infolist = []
        url = start_url + '&page=' + str(1+2*i)
        html = getHTML(url)
        finallist += parsePage(infolist, html)
    
    return finallist

    



result = main()

import pandas as pd

my_df = pd.DataFrame(result)

my_df.to_csv("~/Desktop/jd_apple.csv",encoding='utf_8_sig', index=False, header=False)
