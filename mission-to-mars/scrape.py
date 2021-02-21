#!/usr/bin/env python
# coding: utf-8

def scrape():  
    # dependencies
    import pandas as pd
    import os
    from splinter import Browser
    from bs4 import BeautifulSoup
    from webdriver_manager.chrome import ChromeDriverManager
    from random import randint
    from time import sleep

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #------------------------------------------------------------------------
    # ## NASA News latest headline and p text

    # visit the site
    nasa_news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(nasa_news_url)
    sleep(randint(3,10))

    # preparing soup object
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # get news title
    news_title = soup.find('div', class_='image_and_description_container').find('div', class_='content_title').a.text.strip()

    # get news teaser
    news_p = soup.find(
        'div', class_='list_text').find(
        'div', class_='article_teaser_body').text

    #------------------------------------------------------------------------
    # ## JPL Featured image

    # visit the site
    jpl_img_url = 'https://www.jpl.nasa.gov/images?search=&category=Mars'
    browser.visit(jpl_img_url)
    sleep(randint(3,10))

    # preparing the soup obj
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # finding the most recent image to click into 
    # clicking into the image
    partial_href = soup.find('div', class_='SearchResultCard').find('a', class_='group')['href']
    browser.click_link_by_partial_href(partial_href)
    sleep(10)

    # preparing the soup obj
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # getting the featured image url
    featured_image_url = soup.find('aside').find('a')['href']

    #------------------------------------------------------------------------
    # ## Mars Facts table

    # url for the mars facts website
    mars_facts_url = 'https://space-facts.com/mars/'

    # reading the table to html
    tables = pd.read_html(mars_facts_url)

    # saving the table to a df
    mars_facts_df = tables[0]

    # formatting the df - col names, and setting index
    mars_facts_df.columns = [' ', 'Mars facts']
    mars_facts_df = mars_facts_df.set_index(' ')

    # removing the \n breaks
    mars_table = mars_facts_df.to_html(justify='center').replace('\n', '')


    #------------------------------------------------------------------------
    # ## Hemisphere images

    # visit the site
    hemisphere_img_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_img_url)
    sleep(randint(3,10))

    # preparing the soup obj
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # creating a list of links for the 4 hemispheres
    link_list = []
    for item in soup.find_all('div', class_='description'):
        list_item = item.find('a', class_='itemLink').text
        link_list.append(list_item)

    # appending name of hemisphere and img link
    ## empty list to append dicts of name/img to
    hemisphere_image_urls = []
    ## for loop over the list of links
    for x in range(0, len(link_list)):
        nav_url = link_list[x]
        #print(nav_url)
        # visiting the link for to the hemisphere images
        browser.click_link_by_partial_text(nav_url)

        # prepping the soup object
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        # finding image url and title
        img_url = soup.find('div', class_='downloads').find('a')['href']
        # removing last 9 characters to remove the 'enhanced' end word
        img_title = soup.find('section', class_='block metadata').h2.text[:-9]
        # appending to list of dicts
        hemisphere_image_urls.append({'title': img_title, 'img_url': img_url})

        sleep(randint(1,3))

        # returning to page from which images come to apply next link
        hemisphere_img_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemisphere_img_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        sleep(randint(1,3))


    # quit the browser
    browser.quit()

    return_dict = {
        'nasa_news': {'news_title': news_title, 'news_pp': news_p},
        'jpl_featured_image': featured_image_url,
        'mars_facts_table': mars_table,
        'hemisphere_image_urls': hemisphere_image_urls
    }

    #print(return_dict)
    return return_dict

#scrape()