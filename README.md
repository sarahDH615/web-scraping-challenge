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