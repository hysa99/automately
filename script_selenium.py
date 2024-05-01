from pathlib import Path
import scrapy
from flask import Flask, render_template, request



class QuotesSpider(scrapy.Spider):
    name = "quotes"
  
    def start_requests(self):
        if request.method == 'POST':
            url = request.form['url']
            urls = [url]
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")

