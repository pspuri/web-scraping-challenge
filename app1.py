# import necessary libraries
from flask import Flask, render_template
import pymongo
# import scrape_mars

# create instance of Flask app
app = Flask(__name__)

#create mongo connection
client = pymongo.MongoClient()
db = client.mars_data
collection = db.mars_info

@app.route('/')
def home():
    mars_info = list(db.mars_data.find())    
    return  render_template('index.html',mars_info=mars_info)
# @app.route("/scrape_mars")
# def web_scrape():
#     db.collection.remove({})
#     # mars_data = scrape.scrape()
#     db.collection.insert_one(mars_info)
#     return  render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)