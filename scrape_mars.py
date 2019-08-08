from splinter import Browser
from bs4 import BeautifulSoup
import requests as request
import pandas as pd
from selenium import webdriver
import time


def scrape():
    # create dictionary called mars_data to store scraped data
    browser=Browser("chrome", executable_path='C:\\Users\\suzan\\chromedriver.exe', headless=True)
    news_title, news_p =mars_news(browser)
    mars_data = {
         "news_title": news_title,
         "news_p": news_p,
         "featured_image": featured_image,
         "hemisphers": hemispheres,
         "mars_weather": twitter_weather,
         "mars_facts": mars_facts
    }

    # Stop webdriver and return data
    browser.quit()
    return mars_data

    # Mars - Nasa scrape
def mars_news(browser):
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = request.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_ = 'rollover_description').text
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p

    # Twitter Weather scrape
def twitter_weather(browser):
    url = 'https://twitter.com/marswxreport?lang=en'
    response = request.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    mars_weather = soup.find('div', class_='js-tweet-text-container').text
    mars_data['mars_weather'] = mars_weather

    # Facts scrape
def mars_facts(browser):
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    mars_df = tables[1]
    mars_df.columns = ['Description', 'Value']
    mars_df.set_index('Desctiption', inplace=True)
    
    return mars_df.to_html(classes="table table-striped")
    mars_facts = mars_df.to_html()
    mars_data['mars_facts'] = mars_facts

    # JPL scrape
def featured_image(browser):
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    browser.is_element_present_by_text('more info')
    more_info_elem=browser.find_link_by_partial_text('more info')
    more_info_elem.click()
    
    #Parser with soup
    html= browser.html
    soup = BeautifulSoup(html, "html.parser")
    img_url_rel = soup.select_one('figure.lede a img').get("src")
    img_url_rel

    img_url = f'https://www.jpl.nasa.gov{img_url_rel}'

    return img_url

    # Hemisphere image scrape
def hemispheres(browser):
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)

    hemisphere_html = browser.html
    hemisphere_soup = BeautifulSoup(hemisphere_html, 'html.parser')
    url = 'https://astrogeology.usgs.gov'

    # image urls
    image_list = hemisphere_soup.find_all('div', class_='item')

    # Create list to store dictionaries of data
    hemisphere_image_urls = []

    # Loop to each hemisphere and click link to find image url
    for image in image_list:
        hemisphere_dict = {}
    
        href = image.find('a', class_='itemLink product-item')
        link = url + href['href']
        browser.visit(link)

        #add sleep time to load page
        # time.sleep(2)

        hemisphere_html2 = browser.html
        hemisphere_soup2 = BeautifulSoup(hemisphere_html2, 'html.parser')
    
        img_title = hemisphere_soup2.find('div', class_='content').find('h2', class_='title').text
        hemisphere_dict['title'] = img_title
    
        img_url = hemisphere_soup2.find('div', class_='downloads').find('a')['href']
        hemisphere_dict['url_img'] = img_url
    
        # Append dictionary to list
        hemisphere_image_urls.append(hemisphere_dict)

        #navigate backwards
        browser.back()

    return hemisphere_image_urls

    # store in dictionary
    mars_data['hemisphere_image_urls'] = hemisphere_image_urls

if __name__ == "__main__":
    print(scrape())