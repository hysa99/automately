from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from flask import Flask, render_template, request
from selenium.webdriver.chrome.options import Options
import time
from script_selenium import run_script


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('core.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/open_window', methods=['POST'])
def open_window():
    if request.method == 'POST':
        options = Options()
        options.add_argument("--gui")
        driver = webdriver.Chrome(options=options)
        url = request.form['url']
        driver.get(url)
        print('Opening the window with the url: ' + url)
        time.sleep(10)
        input_=driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
        input_.send_keys('Hello World')
        input_.send_keys(Keys.ENTER)
        time.sleep(10)
        driver.title
        time.sleep(10)
        print('Script executed')
        driver.close()
        print('Window closed')
        return 'home'
    else:
        return 'Error'
    
    


if __name__ == "__main__":
    app.run(debug=True)