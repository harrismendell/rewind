from flask import render_template, g
from models import select_record, get_shop_info
from rewind import app
import sqlite3 as sql

# routes
@app.route('/')
def title_screen():
    return render_template('main.html')

@app.route('/shop')
def shop():
    records = get_shop_info()
    return render_template('shop.html')

@app.route('/record/<recordid>/')
def record(recordid):
    rec = select_record(recordid)[0]
    return render_template('record.html',
                           band=rec[1],
                           record=rec[2],
                           record_cover=rec[3],
                           price=rec[4],
                           current_buyers=rec[5],
                           max_buyers=rec[6],
                           pitchfork_score=rec[7],
                           pitchfork_link=rec[8],
                           review_snippet=rec[9],
                           days_to_go=rec[10]
                           )