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
- Scraping most recent news headline and teaser text from Nasa News website
- Scraping the most recent posted Mars image from JPL (Jet Propulsion Laboratory) Image Gallery website
- Scraping a Mars Facts table from Space Facts website:
- Scraping images of each hemisphere of Mars from Astrogeology government website
- creating a dictionary of all the saved information
- downloading the jupyter notebook as a .py file

scrape.py:
- enclosing the code in a function, scrape
- having the function return the dictionary defined in mission-to-mars.ipynb

#### b. Sending data to MongoDB

files: app.py

- creating a Flask application with a scrape route to connect to Mongo, call scrape.py's scrape() function to scrape new data from the websites, and update Mongo with the new scraping results

#### c. Displaying the data on a webpage

files: app.py, index.html

app.py
- adding a home route to the Flask application that: 1) retrieves data from the Mongo database, 2) sends the information to the html template

index.html
- creating an html template to structure and style the data
    - using bootstrap to place all page elements within a grid and for stylings for buttons and cards
    - creating a header section containing a button linking to the scrape route on the Flask app, for re-scraping data
    - creating a segment that spans the whole page (column size 12) to hold the Nasa headline and teaser text
    - creating two half-page-width segments, one of which holds the Featured Mars Image, and the other holding the Mars Facts table
    - creating a segment to hold the Mars Hemisphere images, each within a Bootstrap card

### challenges

The largest challenge within this project was in scraping the JPL Featured Image. Accessing the full-sized image required finding the most recent link from the Image Gallery page, clicking on that link, and collecting the link to the full-size image. After clicking on the link and going on a new page, it took some time for the webdriver browser and BeautifulSoup to load the new page. This caused both browser and BeautifulSoup to return an Attribute Error when attempting to find the new link within its element 'aside', as the previous webpage did not have that element tag. After some experimentation with placement of pauses in the code (using time.sleep), it appears that pauses between the clicking on the link and the creation of a browser.html object, as well as between creating the browser.html object, and a BeautifulSoup object from parsing the browser object, are necessary. Further sleeps were put into the code after each visit to a new webpage, to guard against overloading the websites, and consequently from being banned from those websites. These sleeps do increase the amount of time it takes for the scraping to occur, and thus, if a user attempts a re-scrape, it will take several minutes for the new scraping results to come in. Further experimentation into how short the sleeps (currently between 3 and 10 seconds) could be cut down to, could be done. 

Another challenge lay in properly rendering the HTML string from the Mars Facts table. Initially, the table was being rendered as a string, rather than a table. Using '|safe' within the fluid HTML on the template allowed for the table to be read properly. Having the table render nicely as a Bootstrap table additionally required changing the to_html() function in scrape.py/mission-to-mars.ipynb to add Bootstrap classes to the HTML string. 

As with the project web-design-challenge, Bootstrap grids proved difficult to work with. The grid system comes with default padding and margin amounts, which meant that creating columns that added up to twelve units in one row were sometimes pushed over to the next line because of accumulated margins. Setting the container to be fluid, and the left margin to be level one ('ml-1') removed this excess, allowing the Featured Mars Image and Mars Facts table to comfortably sit beside each other in one row. 