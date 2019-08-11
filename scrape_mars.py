from splinter import Browser
from bs4 import BeautifulSoup
import requests as request
import pandas as pd

def init_browser():
    executable_path={"executable_path":'C:\\Users\\suzan\\chromedriver.exe'}
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    # create dictionary called mars_data to store scraped data
    browser = init_browser()

    # Mars - Nasa scrape
def mars_news(browser):
    response = request.get('https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest')
    soup = BeautifulSoup(response.text, 'html.parser')

    news_title = soup.find('div', class_='content_title').get_text()
    news_p = soup.find('div', class_ = 'rollover_description').get_text()
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p

    # Twitter Weather scrape
def twitter_weather(browser):
    response = request.get('https://twitter.com/marswxreport?lang=en')
    soup = BeautifulSoup(response.text, 'html.parser')
    mars_weather = soup.find('div', class_='js-tweet-text-container').get_text()
    mars_data['mars_weather'] = mars_weather

    # Facts scrape
def mars_facts(browser):
    tables = pd.read_html('https://space-facts.com/mars/')
    mars_df = tables[1]
    mars_df.columns = ['Description', 'Value']
    mars_df.set_index('Desctiption', inplace=True)
    
    return mars_df.to_html(classes="table table-striped")
    mars_facts = mars_df.to_html()
    mars_data['mars_facts'] = mars_facts

    # JPL scrape
def featured_image(browser):
    browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

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
    mars_data['img_url'] = img_url

    # Hemisphere image scrape
def hemispheres(browser):
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')

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
    
        img_url = hemisphere_soup2.find('img', class_='wide-image').find('src')
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