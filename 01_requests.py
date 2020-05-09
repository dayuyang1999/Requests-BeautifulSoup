import scrapy


class QuotesSpider(scrapy.Spider):  # subclass of scrapy.spider
    name = "quotes"  # user defined
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/random"]   # spider will visit when execute
    
    
    def parse(self, response):   # scrapy will call, when download start_urls
        self.log("I just visited:" + response.url)
        yield{"author_name": response.css("small.author::text")[0].extract(),
              "text": response.css("span.text::text")[0].extract_first(),
              "tags":response.css("a.tag::text").extract() 
             }   # create a dictionary to yield data
        
        
        



import requests

r = requests.get("https://www.amazon.com/dp/B01NAHO017")
r.status_code         # expected status = 200

r.encoding # gussing from header
r.apparent_encoding # gussing from body
r.encoding = r.apparent_encoding

r.text # 



def getHTML(url):
    try:
        r = requests.get(url, timeout = 30)   # >30 seconds, return ERROR
        r.raise_for_status()  # trriger error
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error"
    

if __name__ == "__main__":
    url = "https://www.amazon.com/dp/B01NAHO017"
    print(getHTML(url))








    
        
################## Breaking AMAZON
      
r = requests.get("https://www.amazon.com/dp/B01NAHO017")
r.status_code         # expected status = 200

r.encoding # gussing from header
r.apparent_encoding # gussing from body
r.encoding = r.apparent_encoding

r.text #  we get something back; To discuss automated access to Amazon data please contact api-services-support@amazon.com.\n        For information about migrating to our APIs refer to our Marketplace APIs at https://developer.amazonservices.com/ref=rm_c_sv, or our Product Advertising API at https://affiliate-program.amazon.com/gp/advertising/api/detail/main.html/ref=rm_c_ac for advertising use cases.        
        
## check the header of request

r.request.headers     # honest  tell
 
## edit header

kv  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


url ="https://www.amazon.com/dp/B01NAHO017"
r = requests.get(url, headers = kv)
r.status_code
r.request.headers

r.text
        







######################## Search 

kv = {'q': 'Fuck'}
url = 'http://www.google.com/search'
r = requests.get(url, params = kv)
r.status_code

r.request.url

len(r.text)





####################### picture
path = "/Users/aihuishou/Downloads/pic.jpg"

kv  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = "https://images-na.ssl-images-amazon.com/images/I/71vKA2o0jkL._AC_SL1500_.jpg"
r = requests.get(url, headers = kv)

r.status_code


with open(path, 'wb') as f:
    f.write(r.content)   # write  binary data  to picture, and save into path
    f.close



########  picture, full code
    
import os
url = "https://images-na.ssl-images-amazon.com/images/I/71vKA2o0jkL._AC_SL1500_.jpg"

root = "/Users/aihuishou/Downloads/"

path = root + url.split('/')[-1]

try:
    if not os.path.exists(root): # if root does not exist, create one
        os.mkdir(root)
    

    
    while os.path.exists(path): # if file exists
        lst = path.split('.')
        last =  lst.pop(-1)
        path = '.'.join(lst) + '(1)' + '.' + last

        
    r = requests.get(url, headers=kv)
    with open(path, 'wb') as f:
        f.write(r.content)   # write  binary data  to picture, and save into path
        f.close()
        print("file saved")

except:
    print("something goes wrong")
    
    
        



############################ IP address 
import requests



hack  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = "https://m.ip138.com/iplookup.asp?ip="

r = requests.get(url + '201.204.80.113', headers = hack)
r.status_code
r.encoding = r.apparent_encoding

r.text[-1700:-1500]
