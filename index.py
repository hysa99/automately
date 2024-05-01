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
def start_requesting(self, response):
    if request.method == 'POST':
        url = request.form['url']
        rand_number=random.randint(1, 1000)
        # filename = f"quotes-{rand_number}.html"
        process = CrawlerProcess(get_project_settings())
        process.crawl(QuotesSpider, url=url)
        process.start()
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        return render_template(f"quotes-{page}.html")
    else:
        return 'Error'



if __name__ == "__main__":
    app.run(debug=True)