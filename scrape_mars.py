###----   Import Libraries   ----###     
from bs4 import BeautifulSoup as bs
import requests

from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


def mars_scraper():

    ###----   URL's   ----###
    # NASA Mars News website  
    news_url = "https://redplanetscience.com/"

    # JPL MArs Space Images
    images_url = "https://spaceimages-mars.com/"

    # Mars Facts 
    facts_url = "https://galaxyfacts-mars.com/"

    # Mars Hemispheres 
    hemispheres_url = "https://marshemispheres.com/"


    ###----   Set-up Splinter   ----###
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    ###----   Scrape Mars NASA News         ----###
    ###----   vars = news_title & news_p    ----###    

    browser.visit(news_url)

    html = browser.html
    soup = bs(html, 'html.parser')

    results = soup.find_all('div', class_='list_text')

    for result in results:
        news_title = soup.find('div', class_='content_title').text
        news_p = soup.find('div', class_='article_teaser_body').text


    ###----   Scrape JPL Mars Space Images         ----###
    ###----   vars = feature_img_url    ----###    

    # Open the url
    browser.visit(images_url)

    # Instruct splinter to click on the 'Full Image' link to retrieve full image url
    browser.links.find_by_partial_text('FULL IMAGE').click()

    # Scrape the new page data
    html = browser.html
    soup = bs(html, 'html.parser')

    # Retrieve URL for the full image
    relative_url = soup.find_all('img')[-1]['src']

    # Combine with base URL to get full link
    feature_img_url = images_url + relative_url


    ###----   Pandas Scrape Mars Facts               ----###
    ###----   vars = comparison_table, mars_table    ----###

    # Import the table with pd.read_html
    table = pd.read_html(facts_url)

    # Clean up table 
    comparison_table = table[0]                                            # retrieve the earth/moon comparison table             
    new_headers = comparison_table.iloc[0]                                 # store the first row for the new column names
    comparison_table = comparison_table[1:]                                # remove column names from the main table data 
    comparison_table.columns = new_headers                                 # set the new column names
    comparison_table.set_index('Mars - Earth Comparison', inplace=True)    # reset the index names to the 'comparisons' 

    
    ###----   Scrape Mars Hemispheres    ----###
    ###----   vars = hemi_image_urls     ----###

    # Create empty list to store the scraped data
    hemi_image_urls = []

    # Open the url
    browser.visit(hemispheres_url)

    # Pull the hemisphere names from the page
    html = browser.html
    soup = bs(html, 'html.parser')

    image_links = [] # list to store the hemisphere names

    for name in soup.find_all('h3'):
        image_links.append(name.text)

    image_links = image_links[0:4] # remove the 'Back' element from the list


    # Iterate through each link
    for link in image_links:
        browser.links.find_by_partial_text(link).click()

        html = browser.html
        soup = bs(html, 'html.parser')
    
        # save the link to sample image
        for a in soup.find_all('a', href=True): 
            if a.text == "Sample": 
                sample_url = hemispheres_url + a['href']
        
        # save the link to full high-res image
        for a in soup.find_all('a', href=True): 
            if a.text == "Original": 
                original_url = hemispheres_url + a['href']
    
        # append data to the hemi_image_url list 
        hemi_image_urls.append({'title': link[:-len(' Enhanced')], # removes ' Enhanced' from the title
                                'sample_url': sample_url,
                                'original_url': original_url})
  
        browser.back()

    browser.quit
    
    ###----   Combine vars into dict    ----###
    mars_data = {'news_title': news_title,
                 'news_p': news_p,
                 'feature_img': feature_img_url,
                 'comparison_table': comparison_table.to_dict(),      # df converted to dictionary for mongo
                 'hemi_images': hemi_image_urls}
    
    return mars_data
    

