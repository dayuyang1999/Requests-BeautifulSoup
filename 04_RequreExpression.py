import re



####### re.search
# China Zip
match = re.search(r'[1-9]\d{5}', 'BIT 100081') # return match object


if match:
    print(match.group(0))
  
    
  
    
###### re.match
match = re.match(r'[1-9]\d{5}', 'BIT 100081') # 

match.group(0)   # match is None

match = re.match(r'[1-9]\d{5}', '100081') # 

match.group(0)   # match is match object



###### re.findall 

# return list
lst = re.findall(r'[1-9]\d{5}', 'BIT 100081 TSU 100084') #

lst


###### re.split

re.split(r'[1-9]\d{5}', 'BIT 100081 TSU 100084')
# remove matching part

re.split(r'[1-9]\d{5}', 'BIT 100081 TSU 100084',maxsplit=1)
# return the 1st matching part, and the rest(without split)






###### re.finditer

for m in re.finditer(r'[1-9]\d{5}', 'BIT 100081 TSU 100084'):
    if m:
        print(m.group(0))
    



###### re.sub

re.sub(r'[1-9]\d{5}','zipcode here', 'BIT 100081 TSU 100084')





##################### Match Class

# m is an instanceof Match Class
m = re.search(r'[1-9]\d{5}', 'BIT 100081 TSU 100084')

m.string
m.re #(every regular-expr have to be compiled at first)

m.pos  # matching start point
m.endpos # matching end point

m.start() # match found start point
m.end() # match found end point
m.span()    # match found span






