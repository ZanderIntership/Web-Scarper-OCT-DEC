import requests
import csv
from bs4 import BeautifulSoup

url = input("Enter the url: ")
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
else:
    print("Error, failed to access the url")

soup = BeautifulSoup(html_content, 'html.parser')
titles = soup.find_all('title')

for title in titles:
    print(title.text.strip())


with open('results.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(["Scraped Titles"])
    for title in titles:
        writer.writerow([title.text.strip()])
