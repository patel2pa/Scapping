from bs4 import BeautifulSoup 
import requests
import urllib.request
'''
source = requests.get('https://charlottesville.craigslist.org/d/office-commercial/search/off').text
soup = BeautifulSoup(source, 'lxml')
#blocks = soup.find('li')
#list_of_data = blocks.find('span', class='result-price')
v = 0
y = []
z = []
m = []
n = []
 
v = []
a = []
x = (soup.find_all("li",{"class":"result-row"}))
for tags in x:
    y.append(tags.find_all("span",{"class":"result-price"}))
    z.append(tags.find_all("a", {"class":"result-title hdrlnk"}))
 
for tag in y:
    m.append((tag[0]).text)
for num in z:
    n.append((num[0]).text)
for k in range(len(n)):
    a.append({k:[m[k],n[k]]})
 
#y = (soup.find_all("a",{"class":"result-title hdrlnk"}, text = True))
#for tag in y:
#    print(tag.text)
 
'''
 
 
 

class SearchEngine:
 
    def __init__(self, search_word):
        self.search_word = search_word
        self.headers = {	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'accept-encoding':'gzip, deflate, br',
				'accept-language':'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
				'cache-control':'max-age=0',
				'upgrade-insecure-requests':'1',
				'user-agent':'Chrome/64.0.3282.186'}
 
    def sams(self):
        
        source = requests.get('https://www.samsclub.com/sams/search/searchResults.jsp?searchTerm={}&searchCategoryId=all&xid=hdr_search-typeahead_{}'.format(self.search_word, self.search_word), headers = self.headers)
        soup = BeautifulSoup(source.text, 'lxml')
        x =(soup.find_all("div", {"class":"sc-product-card-title"}))
        y = (soup.find_all("span", {"class": "sc-price"}))
        m = soup.find_all("a", {"class":"sc-product-card-pdp-link"}, href = True)
        products = []
 
        for vals in range(len(x)):
            products.append([(x[vals]).text,(y[vals]).find("span",{"class":"visuallyhidden"}).text, m[vals]['href']])
        print(len(products))
    
    def walmart(self):
        az = []
        bz = []
        source = requests.get('https://www.walmart.com/search/?cat_id=0&grid=true&page=1&query={}&sort=price_low&stores=-1#searchProductResult'.format(self.search_word), headers = self.headers)
        soup = BeautifulSoup(source.text, 'lxml')
        x = soup.find_all("div",{"class":"search-product-result"})
        for results in x:
            y = results.find_all("li")
            for li_tags in y:
                z = li_tags.find_all("div",{"class":"search-result-product-title gridview"})
                try:
                    bz.append(li_tags.find("span", {"class": "price-group price-out-of-stock"})['aria-label'])
                except TypeError:
                    bz.append(0)
                for r in z:
                    az.append([r.find("a").text,r.find("a")['href']])
        for a in range(len(az)):
            az[a].append(bz[a])
        print(az)

        

    def costco(self):
        products = []
        source = requests.get('https://www.costco.com/CatalogSearch?dept=All&keyword={}'.format(self.search_word), headers = self.headers)
        soup = BeautifulSoup(source.text, 'lxml')
        x = soup.find("div",{"class":"container-fluid fixed-container page"})
        y = x.find("div",{"class":"row"}).find("div",{"id":"search-results"}).find("div",{"class":"product-list"}).find_all("div", {"class":"product"})
        for tags in y:
            products.append([tags.find("p",{"class":"description"}).find("a").text, tags.find("div",{"class":"price"}).text, tags.find("p",{"class":"description"}).find("a")['href']])
        
        print(products)
 
'''
 
search_word = 'powerade'
source = requests.get('https://www.samsclub.com/sams/search/searchResults.jsp?searchTerm={}&searchCategoryId=all&xid=hdr_search-typeahead_{}'.format(search_word, search_word))
soup = BeautifulSoup(source.text, 'lxml')
x =(soup.find_all("div", {"class":"sc-product-card-title"}))
y = (soup.find_all("span", {"class": "sc-price"}))
m = soup.find_all("a", {"class":"sc-product-card-pdp-link"}, href = True)
products = []
 
for vals in range(len(x)):
    products.append([(x[vals]).text,(y[vals]).find("span",{"class":"visuallyhidden"}).text, m[vals]['href']])
     
'''  

'''
headers = {	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'accept-encoding':'gzip, deflate, br',
				'accept-language':'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
				'cache-control':'max-age=0',
				'upgrade-insecure-requests':'1',
				'user-agent':'Chrome/64.0.3282.186'}
az = []
bz = []
search_word = 'powerade'
source = requests.get('https://www.walmart.com/search/?cat_id=0&grid=true&page=1&query=powerade&sort=price_low&stores=-1#searchProductResult', headers = headers)
soup = BeautifulSoup(source.text, 'lxml')
x = soup.find_all("div",{"class":"search-product-result"})
for results in x:
    y = results.find_all("li")
    for li_tags in y:
        z = li_tags.find_all("div",{"class":"search-result-product-title gridview"})
        bz.append(li_tags.find("span",{"class":"price-group"})['aria-label'])
        
        for r in z:
            az.append([r.find("a").text,r.find("a")['href']])
for a in range(len(az)):
	az[a].append(bz[a])
        
'''

'''
headers = {	'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
				'accept-encoding':'gzip, deflate, br',
				'accept-language':'en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7',
				'cache-control':'max-age=0',
				'upgrade-insecure-requests':'1',
				'user-agent':'Chrome/64.0.3282.186'}
products = []
search_word = 'powerade'
source = requests.get('https://www.costco.com/CatalogSearch?dept=All&keyword=powerade', headers = headers)
soup = BeautifulSoup(source.text, 'lxml')
x = soup.find("div",{"class":"container-fluid fixed-container page"})
y = x.find("div",{"class":"row"}).find("div",{"id":"search-results"}).find("div",{"class":"product-list"}).find_all("div", {"class":"product"})
for tags in y:
    products.append([tags.find("p",{"class":"description"}).find("a").text, tags.find("div",{"class":"price"}).text, tags.find("p",{"class":"description"}).find("a")['href']])
'''

costco = SearchEngine("gatorade")
print(costco.walmart())









