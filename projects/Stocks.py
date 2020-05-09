import requests
import re
import bs4
#import BeautifulSoup from bs4
import traceback
import pandas as pd
# idea:
# get stock name from page 1
# get exchange info from corresponding pages


def getHTMLText(url):
    hack  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r = requests.get(url, timeout = 30, headers = hack)
    r.encoding = 'utf-8'    
    return r.text




def getStockList(lst, html):
    html_text = getHTMLText(html)
    soup = bs4.BeautifulSoup(html_text, 'html.parser')
    stocks = soup.find_all('tr')
    for i in stocks:
        try:
            stock_name = i.find_all('a', class_ = 'external text')[0].text
            stock_CIK = re.findall(r'\d{10}', i.text)[0]
            lst.append([stock_name,stock_CIK])
        except:
            continue

    return lst[0:50]  # replace this line!


def getStockInfo(lst, stockURL, fpath):
    
    #infoDict = {}
    count = 0
    
    for stock in lst:
        url = stockURL + stock[0]
        html = getHTMLText(url)
        try: 
            if html == '': # sina does not include this
                continue # continue next loop            
            soup = bs4.BeautifulSoup(html, 'html.parser')
            val = soup.find_all('span', attrs={'class':'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})[0].text
            stock.append(val)
            
            # visual prograss bar
            count += 1
            print('\rCurrent Complement:{:.2f}%'.format(count*100/len(lst), end = ''))
        except:
            traceback.print_exc()
            count += 1
            print('\rCurrent Complement:{:.2f}%'.format(count*100/len(lst), end = ''))
            continue
    
    my_df = pd.DataFrame(lst)
    my_df.to_csv("~/Desktop/sp500.csv",encoding='utf_8_sig', index=False, header=False)

    
    return lst




def main():
    stock_list_url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies' 
    stock_info_url = 'https://finance.yahoo.com/quote/'
    output_file = '~/Desktop/SP500.txt'
    
    slist = []  # store stock list
    slist = getStockList(slist, stock_list_url) # 
    result = getStockInfo(slist, stock_info_url, output_file)
    
    return result



main()






