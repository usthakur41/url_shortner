import sqlite3
import string
import json
from random import choice
from hashids import Hashids
from flask import Flask, render_template, request, flash, redirect, url_for


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
chars = string.ascii_letters
random =  ''.join(choice(chars) for _ in range(4))
app.config['SECRET_KEY'] = random

hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])

def response(body = {}, error = '', msg = ''):
	resp = {
		'body': body,
		'error': error,
		'msg': msg
	}
	return json.dumps(resp)
@app.route('/url/<string:url>', methods=('POST',))
def index(url):
    conn = get_db_connection()

    if request.method == 'POST':

        if not url:
            error = 'The URL is required!'
            return response(error = [error]), 404

        url_data = conn.execute('INSERT INTO urls (original_url) VALUES (?)',
                                (url,))
        conn.commit()
        conn.close()

        url_id = url_data.lastrowid
        hashid = hashids.encode(url_id)
        short_url = request.host_url + hashid
        
        msg = 'Success'
        body = short_url
        return response(body = body, msg = msg), 200



