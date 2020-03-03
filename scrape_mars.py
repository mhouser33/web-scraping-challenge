# import dependencies
import requests
import pymongo
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
from pprint import pprint
import time

# open chrome driver browser
executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
browser = Browser('chrome', **executable_path, headless=False)

# define url
mars_news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
browser.visit(mars_news_url)

# create beautiful soup object 
html = browser.html
mars_news_soup = bs(html, 'html.parser')

# find the first news title
news_title = mars_news_soup.body.find("div", class_="content_title").text

# find the paragraph associated with the first title
news_paragraph = mars_news_soup.body.find("div", class_="article_teaser_body").text

# close the browser
print(f"The news title is: \n{news_title}")
print('----------------------------------------------------------------------------------------')
print(f"The paragraph is:  \n{news_paragraph}")

# Mars Images
# define the url and visit it with browser
featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(featured_image_url)

#Click on the the button to get to the full image
full_image=browser.find_by_id('full_image')
full_image.click()
time.sleep(2)
browser.click_link_by_partial_text('more info')

#find image url to full size
html_image = browser.html

#Parse with 'html.parser
soup = bs(html_image, 'html.parser')

#Retrieve image from style tag
#Scrape url
img_url = soup.find('img', class_ = 'main_image')['src']
featured_img_url = "https://www.jpl.nasa.gov" + img_url
print(featured_img_url)

# Open Mars Weather Twitter URL in browser
mars_weather_url = "https://twitter.com/marswxreport?lang=en"
browser.visit(mars_weather_url)
time.sleep(1)

#Create Soup Item
html_weather = browser.html
soup = bs(html_weather, 'html.parser')

#Save Most Recent Weather String Tweet.
mars_weather = soup.find_all('div', class_='js-tweet-text-container')
print(mars_weather)

# Define url
space_facts_url = "https://space-facts.com/mars/"

# Read html into pandas
tables = pd.read_html(space_facts_url)

space_df = tables[0]
space_df.columns = ["Description", "Value"]
space_df

# Convert to html table
space_facts_html=space_df.to_html()
space_facts_html

# Mars Hemispheres
# Define url and open in browser
mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_hemispheres_url)

# Sciaperelli Hemishere
# Define url and open in browser
mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_hemispheres_url)

# Click on the link for the hemisphere
browser.click_link_by_partial_text('Schiaparelli')

# Click on the open button enhanced
browser.click_link_by_partial_text('Open')

# Create soup item
schiaparelli_html = browser.html
schiaparelli_soup = bs(schiaparelli_html, 'html.parser')
schiaparelli = schiaparelli_soup.body.find('img', class_ = 'wide-image')
schiaparelli_img = schiaparelli['src']
hem_base_url = 'https://astrogeology.usgs.gov'
schiaparelli_url = hem_base_url + schiaparelli_img
print(schiaparelli_url)

# Cerberus Hemisphere# 
# Define url and open in browser
mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_hemispheres_url)

# Click on the link for the Cerberus hemisphere
browser.click_link_by_partial_text('Cerberus')

# Click on open button to get to enhanced picture
browser.click_link_by_partial_text('Open')

# Create a soup item
hemispheres_html = browser.html
cerberus_soup = bs(hemispheres_html, 'html.parser')
cerberus = cerberus_soup.body.find('img', class_ = 'wide-image')
cerberus_img = cerberus['src']
hem_base_url = 'https://astrogeology.usgs.gov'
cerberus_url = hem_base_url + cerberus_img
print(cerberus_url)

# Define url and open in browser
mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_hemispheres_url)

# Syrtis Hemisphere# %%
# Define url and open in browser
mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_hemispheres_url)

# Click on the link for the Cerberus hemisphere
browser.click_link_by_partial_text('Syrtis')

# Click on the link for the Cerberus hemisphere
browser.click_link_by_partial_text('Open')

# Create a soup item
syrtis_html = browser.html
syrtis_soup = bs(syrtis_html, 'html.parser')
syrtis = syrtis_soup.body.find('img', class_ = 'wide-image')
syrtis_img = syrtis['src']
hem_base_url = 'https://astrogeology.usgs.gov'
syrtis_url = hem_base_url + syrtis_img
print(syrtis_url)

# Valles Hemisphere
# Define url and open in browser
mars_hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
browser.visit(mars_hemispheres_url)

# Click on the link for the Cerberus hemisphere
browser.click_link_by_partial_text('Valles')

# Create a soup item
valles_html = browser.html
valles_soup = bs(valles_html, 'html.parser')
valles = valles_soup.body.find('img', class_ = 'wide-image')
valles_img = valles['src']
hem_base_url = 'https://astrogeology.usgs.gov'
valles_url = hem_base_url + valles_img
print(valles_url)

hemispheres_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_url},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_url},
        {"title": "Schiaparelli Marineris Hemisphere", "img_url": schiaparelli_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_url}
    ]
hemispheres_image_urls

# Dictionaries for hemispheres# %%
hemispheres_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_url},
        {"title": "Cerberus Hemisphere", "img_url": cerberus_url},
        {"title": "Schiaparelli Marineris Hemisphere", "img_url": schiaparelli_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_url}
    ]
hemispheres_image_urls

mars_dictionary = [
    {'currentheadline': news_title},
    {'currentparagraph':  news_paragraph},
    {'featuredimage': featured_img_url},
    {'currentweather': mars_weather},
    {'facts': space_facts_html},
    {"valles_title": "Valles Marineris Hemisphere", "img_url": valles_url},
    {"cerberus_title": "Cerberus Hemisphere", "img_url": cerberus_url},
    {"schiaperelli_title": "Schiaparelli Marineris Hemisphere", "img_url": schiaparelli_url},
    {"syrtis_title": "Syrtis Major Hemisphere", "img_url": syrtis_url} 
]
mars_dictionary
browser.quit()
