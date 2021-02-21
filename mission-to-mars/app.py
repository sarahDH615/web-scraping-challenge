# 1. imports
from flask import Flask
import sys
import os
import pymongo

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    #extra imports
    from bson import json_util, ObjectId
    import json

    # estb connection
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    
    # connect to the db marsDB
    db = client.marsDB

    # create a variable for the (presumably one entry)
    mars_info = db.mars_info.find()

    # save any entries to a list
    mars_info_list = []
    for entry in mars_info:
        mars_info_list.append(entry)
    
    # save the first and only entry as a variable for html use
    mars_entry = mars_info_list[0]

    mars_sanitised = json.loads(json_util.dumps(mars_entry))
    return mars_sanitised



# 4. Define what to do when a user hits the /about route
@app.route("/scrape")
def do_scrape():
    # importing scrape function
    from scrape import scrape

    #running scrape
    mars_dict = scrape()

    # connecting to mongo to insert in db collection
    # estb connection
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    
    # connect to the db marsDB
    db = client.marsDB

    # getting rid of the collection mars_info if it already exists
    collist = db.list_collection_names()
    if 'mars_info' in collist:
        db.mars_info.drop()

    # inserting the results of scrape into the collection
    db.mars_info.insert_one(mars_dict)

    return 'Scraping and entry complete!'


if __name__ == "__main__":
    app.run(debug=True)
