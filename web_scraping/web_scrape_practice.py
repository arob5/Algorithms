#
# web_scrape_practice.py
# Practicing Web Scraping by following DataSchools web scraping tutorial
# Last Modified: 8/7/2017
# Modified By: Andrew Roberts
#

from bs4 import BeautifulSoup
import requests

# Get request and pass HTML code to BeautifulSoup
r = requests.get("https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html")
soup = BeautifulSoup(r.text, "html.parser")

results = soup.find_all("span", attrs={"class":"short-desc"})
