Web Page Title Scraper
Overview

This Python script extracts the <title> tag(s) from a web page and saves them into a CSV file. It is useful for basic web scraping practice or quickly capturing page titles for analysis.

The script:

Prompts the user for a URL

Downloads the web page content

Extracts all <title> elements

Prints the titles to the console

Saves the titles to a file called results.csv

Requirements

Before running the script, make sure you have the following installed:

Python 3.8+

Required Python libraries:

requests

beautifulsoup4

Install dependencies using:

pip install requests beautifulsoup4

How to Use

Save the script as a Python file (for example: title_scraper.py)

Open a terminal or command prompt

Run the script:

python title_scraper.py


When prompted, enter a full URL (including https://), for example:

Enter the url: https://www.example.com

Output
Console Output

The script prints the extracted title(s) directly to the console:

Example Domain

CSV File

A file named results.csv is created in the same directory as the script.

Example contents of results.csv:

Scraped Titles
Example Domain
