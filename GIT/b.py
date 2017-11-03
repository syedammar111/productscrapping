import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
#my_url = 'https://www.newegg.com/Weekend-Deals/EventSaleStore/ID-969?cm_sp=Herobottombanner1-_-nepro%252f17-7568-_-%2f%2fpromotions.newegg.com%2fnepro%2f17-7568%2fhomepage_300x120.jpg&icid=416925'
my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=StoreIM&Depa=1&Category=38'

# opening up connection and grabbing the page
uClient =  ureq(my_url)
page_html = uClient.read()
uClient.close()


# html parsing
page_soup = soup(page_html,"html.parser")

# grabs each product
containers = page_soup.findAll("div",{"class": "item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)


for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a",{"class" : "item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class" : "price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand:" + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

f.write(brand + "," + product_name.replace(",","|") + "," + shipping + "\n")

f.close()