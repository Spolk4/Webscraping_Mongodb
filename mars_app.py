from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo 


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.mars_data.find_one()
    return render_template('mars_index.html', mars_data=mars_data)

@app.route("/scrape")
def scraped():
    mars_data = mongo.db.mars_data
    mars_data_scrape = mars_data.scrape_all()
    mars_data.update(
        {},
        mars_data_scrape,
        upsert=True
    )
    return "Scraping Successful"

if __name__ == "__main__":
    app.run(debug=True)