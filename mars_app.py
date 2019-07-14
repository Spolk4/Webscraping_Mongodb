from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app)

@app.route("/")
def index():
    try:
        mars_data = mongo.db.mars_data.find_one()
        return render_template('index.html', mars_data=mars_data)
    except:
        return redirect("http://localhost:5000/scrape", code=302)

@app.route("/scrape")
def scraped():
    mars_data = mongo.db.mars_data
    mars_data_scrape = scrape_mars.scrape()
    mars_data.update(
        {},
        mars_data_scrape,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
    
from splinter import Browser
with Browser()as browser:
#visit URL
url = "http://www.google.com"
browser.vist(url)
browser.fil('q', 'splinter- python acceptance testing for web applications')
#Find and click the 'search' buttons
button= browser.find_by_name(btnG')
#interact with elements
button.click()
if browser.is_test_present('splinter.readthedocs.io'):
    print("Yes, the official wesite was found!")
 else:
    print("No, it wasn't found... We need to improve our SEO techniques")
    
Sample splinter and beautiful soup code
from splinter import Browser
from bs4 import BeautifulSoup

executable_path = {'executable_path':'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

url= "https://quotes.toscrape.com/
browser.visit(url)

for x in range (1,6):   <-----these represent the page range
    html = browser.html
    soup = beautifulSoup(html, 'html.parser')
    
    quotes = soup.find_all('span', class_='text)
    
    for quote in quotes:
        print('page:', x, '------')
        print(quote.text)
        
    browser.click_link_by_partial_text('Next')   <------look into the documentation from splinter for this, it moves through all the pages and prints them
(what is regression?)
Mars weather twitter account (https://twitter.com/marswxreport?lang=en) and save latest tweet for the weather report as a variable called mars_weather
mars facts webpage to scrape containing facts about the planet (https://space-facts.com/mars/) - use pandas to convert to an html table string
mars astrogeology (https://wustl.bootcampcontent.com/wustl-bootcamp/WUSTL201904DATA2/tree/master/02-Homework/12-Web-Scraping-and-Document-Databases/Instructions)
use img_url = 
use title = 
append the sictionary with the image url string and the hemisphere title to a list (a dictionary for each hemisphere)
hemisphere_image_urls = [{"title": "Valles Marineris Hemisphere", "img_url":""}, 
                        {"title": "Cerberus Hemisphere", "img_url":""}, 
                        {"title": "Schiaparelli Hemisphere", "img_url":""}, 
                        {"title": "Syrtis Major Hemisphere", "img_url":""}
                        ]

Step2
covert jupyter notebook into Python script called scrape_mars.py with scrape that will return the Python Dictionary with all the scraped data
create a route calld /scrape that import scrape_mars.py  and call your scrape function stor in Mongo as python dict
@app.route/scrape

from bs4 import BeautifulSoup
import requests
import pymongo

#initialize Pymongo to work with MongoDBs
conn = 'mongodb://localhost:27017
client = pymongo.MongoClient(conn)

db = clinet.craigslist_db
collection = db.items

#url of the page
url = 'https//


#
