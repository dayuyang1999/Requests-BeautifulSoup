#### three steps:
#   1. get html 
#   2. put html to lst
#   3. print lst




import requests
from bs4 import BeautifulSoup
import bs4



#### define help function

def getHTMLText(url):
    try:
        hack = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        r = requests.get(url, timeout = 30, headers = hack)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'something goes wrong'  # blank 
    


def fillUnivList(ulst, html_text):   # parser
    soup = BeautifulSoup(html_text, 'html.parser')
    
    # all univ info store in <tbody>
    for tr in soup.find( name = 'tbody').contents:  #iterator
        # each univ, each loop
        univ = []
        # childeren could be string or lower tags
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')
            # for td
            for td in tds:
                univ.append(td.string)
            ulst.append(univ)
    
    
    return ulst
    
    
    

            


 

 

#### define MAIN function

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/BCSR/yingyongjingjixue2019.html'
    html_text = getHTMLText(url)
    return fillUnivList(uinfo, html_text) # return a list


    
    
    
    
    
    
    
    
    
    
    