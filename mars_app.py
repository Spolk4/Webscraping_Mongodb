from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo 
import mars_data

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars= mongo.db.mars.find_one()
    print(mars)
    return render_template('mars_index.html', mars_data=mars_data)

@app.route("/scrape")
def scraped():
    mars = mongo.db.mars
    mars_scrape = mars_data.scrape_all()
    mars.update(
        {},
        mars_scrape,
        upsert=True
    )
    return "Scraping Successful"

if __name__ == "__main__":
    app.run(debug=True)