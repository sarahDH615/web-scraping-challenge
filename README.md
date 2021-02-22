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

#### b. Sending data to MongoDB

files: app.py

- creating a Flask application with a scrape route
    - connecting to a Mongo database and creating a collection, mars_info, if it does not already exist
    - calling scrape.py's scrape() function to scrape new data from the websites
    - updating the database with the scraping results
    - returning the user back to the home route

#### c. Displaying the data on a webpage

files: app.py, index.html

app.py
- adding a home route to the Flask application that: 1) retrieves data from the Mongo database, 2) sends the information to the html template
    - connecting the the Mongo database and retrieving the record from the collection mars_info
    - separating out the different items in the returned dictionary and saving them to variables
    - sending those variables to the index.html template using render_template()

index.html
- creating an html template to structure and style the data
    - linking bootstrap as a stylesheet
        - using bootstrap to place all page elements within a grid
        - using stylings for buttons and cards
    - creating a header section containing a button linking to the scrape route on the Flask app, for re-scraping data
    - creating a segment that spans the whole page (column size 12) to hold the Nasa headline and teaser text
    - creating two half-page-width segments, one of which holds the Featured Mars Image, and the other holding the Mars Facts table
    - creating a segment to hold the Mars Hemisphere images, each within a Bootstrap card
