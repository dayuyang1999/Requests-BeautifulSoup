
########### Beautiful Soup################3


import requests 

hack  = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

url = "https://python123.io/ws/demo.html"

r = requests.get(url , headers = hack)
r.status_code


r.encoding = r.apparent_encoding


from bs4 import BeautifulSoup

soup = BeautifulSoup(r.text, 'html.parser')







################   WHAT IS TAG ##############


### get tags 

# tag a is hyperlink in html

type(soup.a)

### get name of tags
soup.a.parent.name #tag
soup.a.name
soup.a.parent.parent.name


### # get dictionary of tags
soup.a.attrs  
# like dict
soup.a.attrs["href"]

########## get string of tags
soup.a.string
soup.p.string



# tag b (comment)

html2 = """<b><!-- This is a comment --></b>
<p>This is not a comment</p>"""

soup2 = BeautifulSoup(html2, 'html.parser')

type(soup.b)
soup2.b.string











### Tree structure of html doc #####################





##################### from root to leaf

soup = BeautifulSoup(r.text, "html.parser")



 # head tag
soup.head 

next(soup.head.children)  # childrens (iterator)
# or contents
soup.head.contents  # a list


# body tag

soup.body.contents # lst
len(soup.body.contents) # how many tags

soup.body.contents[1]



# traverse all elements

for child in soup.body.contents:
    print(child)
    
for parents in soup.body.descendants:
    print(parents)







    
##################### from leaf to root


soup.title.parent  # expected to be "head tag"

# what is the parent of the root(html tag)
soup.html.parent # return root itself


##### 
# print names of the parents of soup.a

for parent in soup.a.parents:
    if parent is None: # soup pbject has no .name method 
        print(parent)
    else:
        print(parent.name)







#####################  parallel 

soup.a.next_sibling  # parallel 1   WARNING It is a String!
soup.a.next_sibling.next_sibling # # parallel 2

soup.a.previous_sibling # parallel -1  WARNING it is a string!!!
soup.a.previous_sibling.previous_sibling # parallel -2

soup.a.parent # expected to be p tag



### traverse
for sibling in soup.a.next_siblings:
    print(sibling)
    
    
    












#################### Prettify ###################3

# prettify an entire bs object
soup.prettify()  # add line breaks
print(soup.prettify())


# prettify a tag

print(soup.a.prettify())
    








############################## Marker ########################################



