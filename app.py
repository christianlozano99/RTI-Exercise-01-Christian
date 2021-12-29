from flask import Flask, render_template
from flask_paginate import Pagination, get_page_args
import pandas as pd

app = Flask(__name__)

#Pulling in data to pandas array
csv = pd.read_csv('static/extractedData.csv')

#Changing over_50k to csv for easy viewing
csv['over_50k'] = csv['over_50k'].replace({1:'Yes', 0: 'No'})
data = csv.to_dict(orient = 'records')

# Gets Entries in data so it doesnt load whole csv
def get_users(offset=0, per_page=20):
    return data[offset: offset + per_page]

#Pagniated view page
@app.route("/")
def index():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    total = len(data)

    pagination_users = get_users(offset=offset, per_page=per_page)

    pagination = Pagination(page=page, 
                            per_page=per_page, 
                            total=total,
                            css_framework='bootstrap4')

    return render_template('index.html',
                           data=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)

#Pagniated view page
@app.route("/ExploratoryAnalysis")
def ExploratoryAnalysis():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')

    total = len(data)

    pagination_users = get_users(offset=offset, per_page=per_page)

    pagination = Pagination(page=page, 
                            per_page=per_page, 
                            total=total,
                            css_framework='bootstrap4')

    return render_template('html/ExploratoryAnalysis.html',
                           data=pagination_users,
                           page=page,
                           per_page=per_page,
                           pagination=pagination)

if __name__ == "__main__":
    app.run(debug = True,threaded=True)