import urllib2
from BeautifulSoup import BeautifulSoup

url = "http://espn.go.com/"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

nba = soup.first("li", { 'id':'menu-nba'})

nba_link = nba.first()
nba_url = nba_link["href"]

nba_page = urllib2.urlopen(nba_url)
soup = BeautifulSoup(nba_page).first("div", "nav-main-secondary")

item = soup('li', limit=2)[1]

print item.first("a")["href"]