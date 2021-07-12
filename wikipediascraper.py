#Importing Packages 
import csv

from bs4 import BeautifulSoup
import requests


# Empty array for Data
rows =[]


#open the website
url = "https://en.wikipedia.org/wiki/Category:Women_computer_scientists"
page = requests.get(url)
paghe_content = page.count


#parse the page with the Beautiful Soup Library
soup = BeautifulSoup(page_content, "html.parser")
content = soup.find("div", class_="mw-category")
all_groupings = content.find_all("div", class_="mw-category-group")
for grouping in all_groupings:
name_list = grouping.find("ul")
category = grouping.find("h3"),get_text()
alphabetical_names = names_list.find_all("li")

for alphabetical_name in alphabetical_names:
#get the name
name = alphabetical_name.find("a",href = True)
link anchortag["href"]
#get the letter
letter_name = category 