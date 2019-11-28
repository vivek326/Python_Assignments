from requests import get
from bs4 import BeautifulSoup
url='https://www.moneycontrol.com/'
response=get(url)

soup=BeautifulSoup(response.text,'html.parser')
'''lxml'''

'''
#All Company Names
tables=soup.find_all('table',class_="rhsglTbl")
for table in tables:
    links=table.find_all('a')
    #print(links)
    for link in links:
        print(link.get('title'))'''

losers = soup.find_all('div',attrs={'id':'tlNifty'})
print("Losers Nifty")
for loser in losers:
    links = loser.find_all('a')
    for link in links[:-1]:
        print(link.get('title'))
print ("--------------------------------------------------")
losers = soup.find_all('div',attrs={'id':'tlSensex'})
print("Losers-Sensex")
for loser in losers:
    links = loser.find_all('a')
    for link in links[:-1]:
        print(link.get('title'))