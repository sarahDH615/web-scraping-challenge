# 1. imports
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape


# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/marsDB"
mongo = PyMongo(app)

# home route
@app.route("/")
def home():
    #extra imports
    from bson import json_util, ObjectId
    import json
    
    mars_data = mongo.db.mars_info.find_one()

    return render_template(
        'index.html', 
        nasa_title = mars_data['nasa_news']['news_title'],
        nasa_pp = mars_data['nasa_news']['news_pp'],
        jpl_img = mars_data['jpl_featured_image'],
        table = mars_data['mars_facts_table'],
        hemi1title = mars_data['hemisphere_image_urls'][0]['title'],
        hemi1url = mars_data['hemisphere_image_urls'][0]['img_url'],
        hemi2title = mars_data['hemisphere_image_urls'][1]['title'],
        hemi2url = mars_data['hemisphere_image_urls'][1]['img_url'],
        hemi3title = mars_data['hemisphere_image_urls'][2]['title'],
        hemi3url = mars_data['hemisphere_image_urls'][2]['img_url'],
        hemi4title = mars_data['hemisphere_image_urls'][3]['title'],
        hemi4url = mars_data['hemisphere_image_urls'][3]['img_url'],
        )

# scrape route
@app.route("/scrape")
def do_scrape():
    mars_info = mongo.db.mars_info
    new_mars_data = scrape.scrape()
    mars_info.update({}, new_mars_data, upsert=True)

    return redirect('/', code=302)
    
if __name__ == "__main__":
    app.run(debug=True)
