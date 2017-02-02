import urllib2
from bs4 import BeautifulSoup

url = raw_input('http://asia.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=ENSG00000141510;r=17:7661779-7687550')

html = urllib2.urlopen('http://' +url).read()
soup = BeautifulSoup(html)
soup.prettify()
for anchor in soup.findAll('div', href=True):
    print anchor['href']

