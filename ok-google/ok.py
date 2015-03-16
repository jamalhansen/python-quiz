import urllib2
import string
from BeautifulSoup import BeautifulSoup

question = raw_input('Ask your Question: ')

# remove everything but spaces, numbers and letters
clean = "".join([c for c in question if c in string.letters or c.isdigit() or c in string.whitespace])

# now make a list of the words
word_list = clean.split(" ")

# if there were multiple spaces in a row we have list elements that are "", let's remove them
while "" in word_list:
    word_list.remove("")

# create the list again with plusses
query = "+".join(word_list)

url = "http://google.com?nojs=1&q=" + query

page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

print soup.find(id="")
