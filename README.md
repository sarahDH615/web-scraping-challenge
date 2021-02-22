## web-scraping-challenge

### contains
- mission to mars:
    - templates:
        - index.html: html template for flask application
    - app.py: flask application displaying the results of scrape.py using index.html
    - flask_app_screenshot_combination.pdf: screenshots of the sections of the flask application page, combined to mimic the appearance of the webpage itself
    - mission-to-mars.ipynb: Jupyter Notebook from which scrape.py was derived
    - scrape.py: a script to access webpages and append content to a Mongo DataBase as a python dictionary

### description

The purpose of this project was to create a single webpage that had information relating to the Mars expedition selected from several webpages. The overall structure of the work was using Beautiful Soup and Splinter to scrape data from the webpages, sending the data to a MongoDB collection, and using Flask to display the information and commence new scrapes. These stages are explained below in greater detail.

#### a. Scraping

files: mission-to-mars.ipynb, scrape.py (export)

mission-to-mars.ipynb:
- Scraping most recent news headline and teaser text from Nasa News website using BeautifulSoup.find()
- Scraping the most recent posted Mars image from JPL (Jet Propulsion Laboratory) Image Gallery website:
    - using BeautifulSoup.find() to find the most recent image's link
    - using browser.click_link_by_partial_href to click into that link and append a full-size image
- Scraping a Mars Facts table from Space Facts website:
    - using pd.read_html to access tabular content
    - saving the table as a dataframe to format the table
    - converting the dataframe to an html string using pd.to_html
        - adding bootstrap classes to the html string and cleaning the string
- Scraping images of each hemisphere of Mars from Astrogeology government website:
    - using BeautifulSoup.find_all() to create a list of links to the 4 hemisphere images
    - looping over the list of links, clicking on each link, and using BeautifulSoup.find() to find full sizze images
    - saving the images and titles to a list of dictionaries
- creating a dictionary of all the saved information
- downloading the jupyter notebook as a .py file

scrape.py:
- enclosing the code in a function, scrape
- having the function return the dictionary defined in mission-to-mars.ipynb
