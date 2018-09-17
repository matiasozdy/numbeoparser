#!/usr/bin/python
import requests
import sys
from bs4 import BeautifulSoup
from pprint import pprint
from terminaltables import AsciiTable
from operator import itemgetter

table = [['City', 'Monthly cost', 'Currency']]
cities = ["London", "Barcelona", "Madrid", "Berlin", "Munich", "Malaga", "Rome", "Frankfurt", "Hamburg", "Granada", "Prague", "Budapest", "Amsterdam"]
#cities = ["London", "Barcelona", "Madrid"] #FOR TESTING
for city in cities:
    url = 'https://www.numbeo.com/cost-of-living/city-estimator/in/' + city + '?displayCurrency=EUR&members=2&restaurants_percentage=5.0&inexpensive_restaurants_percentage=10.0&drinking_coffee_outside=30.0&going_out_monthly=0&smoking_packs_per_day=0.0&alcoholic_drinks=0.0&type_of_food=0&driving_car=0.0&taxi_consumption=0.0&paying_for_public_transport=Monthly%252C+All+Members&sport_memberships=0.0&vacation=0.0&clothing_and_shoes=50.0&rent=27&kindergarten_count=0&private_schools_count=0'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    thhigh = soup.find_all('th', class_='th_no_highlight_a_right')[-1].get_text().split(' ')
    thhighdiv = thhigh[1].replace(u'\xa0', u' ').split(' ')
    table.append([city, thhighdiv[0], thhighdiv[1]])
options = url.split('?')
options = options[1].split('&')
opttable = [["Option", "Value"]]
for option in options:
  opt = option.split('=')
  opttable.append([opt[0], opt[1]])
optable = AsciiTable(opttable)
table = AsciiTable(table)
if (len(sys.argv) > 1):
    print optable.table
print table.table
