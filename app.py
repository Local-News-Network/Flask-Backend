from flask import Flask, render_template, request
import requests
import itertools
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['country']
        print(os.getenv("API_KEY"))
        # Now, we will call the NewsAPI with country as the query
        url = ('https://newsapi.org/v2/top-headlines?'
               'country=' + data + '&'
               f'apiKey={os.getenv("API_KEY")}')
        r = requests.get(url)
        dict = r.json()
        # return dict
        return render_template('home.html', country=data, len = 18, country_list = dict)
    else:
        return render_template('index.html');

# @app.route('/country/<data>')
# def get_js_data(data):
#     return render_template('home.html', country=data)

# @app.route('/country', methods = ['POST'])
# def get_post_data():
#     country = request.form['data']
#     return country

if __name__ == "__main__":
    app.run(debug=True)
