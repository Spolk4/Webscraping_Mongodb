from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests as request
import pandas as pd

def init_browser():
    executable_path = {'executable_path': 'C:\\Users\\suzan\\chromedriver.exe'}
    return Browser("chrome", **executable_path, headless = False)

def scrape():
    # create dictionary called mars_data to store scraped data
    browser = init_browser()
    mars_data = {}

    # Mars - Nasa scrape
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = request.get(url)
    soup = bs(response.text, "lxml")

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_ = 'article_teaser_body').text
    mars_data['news_title'] = news_title
    mars_data['news_p'] = news_p

    # Weather scrape
    url = 'https://twitter.com/marswxreport?lang=en'
    response = request.get(url)
    soup = bs(response.text, 'lxml')
    mars_weather = soup.find('div', class_='js-tweet-text-container').text
    mars_data['mars_weather'] = mars_weather

    # Facts scrape
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    mars_df = tables[1]
    mars_df.columns = ['Description', 'Value']
    html_mars = mars_df.to_html()
    mars_data['html_mars'] = html_mars

    # use splinter
    browser = init_browser()

    # JPL scrape
    jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(jpl_url)

    jpl_html= browser.html
    soup = bs(jpl_html, "lxml")

    featured_image = soup.find('div', class_='default floating_text_area ms-layer').find('footer')
    featured_image_url = 'https://www.jpl.nasa.gov'+ featured_image.find('a')['data-fancybox-href']
    mars_data['featured_image_url'] = featured_image_url
    
    # Hemisphere image scrape
    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)

    hemisphere_html = browser.html
    hemisphere_soup = bs(hemisphere_html, 'lxml')
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

        hemisphere_html2 = browser.html
        hemisphere_soup2 = bs(hemisphere_html2, 'lxml')
    
        img_title = hemisphere_soup2.find('div', class_='content').find('h2', class_='title').text
        hemisphere_dict['title'] = img_title
    
        img_url = hemisphere_soup2.find('div', class_='downloads').find('a')['href']
        hemisphere_dict['url_img'] = img_url
    
        # Append dictionary to list
        hemisphere_image_urls.append(hemisphere_dict)
      
    # store in dictionary
    mars_data['hemisphere_image_urls'] = hemisphere_image_urls

    return mars_data