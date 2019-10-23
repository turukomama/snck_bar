import urllib.request, urllib.error
from bs4 import BeautifulSoup
 
url = "http://www.yahoo.co.jp"
htmlfp = urllib.request.urlopen(url)
html = htmlfp.read().decode("utf-8", "replace")
htmlfp.close()
 
soup = BeautifulSoup(html)
for link in soup.findAll("a"):
	print (link)