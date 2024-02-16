import requests
from bs4 import BeautifulSoup

req = requests.get('https://news.ycombinator.com/')
reqcontent = req.content
newsoup = BeautifulSoup(reqcontent, 'html.parser')

# Find all 'span' tags with 'titleline' class, then find the nested 'a' tag within
for title_span in newsoup.find_all('span', {'class': 'titleline'}):
    link = title_span.find('a', href=True)
    if link:
        print(f"{link.text}\n\n{link['href']}\n\n")

input('Type anything to quit: ')
