from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from flask import Flask, render_template, request, redirect, url_for
from selenium.webdriver.chrome.options import Options
import random
from script_selenium import QuotesSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.signalmanager import dispatcher
from scrapy import signals
from pathlib import Path
from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('core.html')

@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/start_requesting', methods=['POST']) 
def start_requesting():
    if request.method == 'POST':
        url = request.form['url']
        filename = "quotes-form.html"
        process = CrawlerProcess(get_project_settings())
        process.crawl(QuotesSpider, url=url, filename=filename)
        process.start()
        return render_template(filename) # Example: rendering a template for the form
    else:
        return 'Method Not Allowed', 405
    



if __name__ == "__main__":
    app.run(debug=True)