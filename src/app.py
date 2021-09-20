import sqlite3
import string
import json
from random import choice
from hashids import Hashids
from flask import Flask, render_template, request, flash, redirect, url_for


def get_db_cursorection():
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
    conn = get_db_cursorection()
    cursor=conn.cursor()

    if request.method == 'POST':
        short_url = ''

        cursor.execute('SELECT id FROM urls WHERE original_url = (?)', (url,))
        data = cursor.fetchone()
        if data is None:
            url_data = cursor.execute('INSERT INTO urls (original_url) VALUES (?)',
                                (url,))
            url_id = url_data.lastrowid
            hashid = hashids.encode(url_id)
            cursor.execute('SELECT id FROM urls WHERE original_url = (?)', (url,))
            data = cursor.fetchone()
            url_id = data[0]
            url_data = cursor.execute(' INSERT INTO hash_table(hash_id, url_id) VALUES (?,?)',(hashid,url_id,))
            short_url = request.host_url + hashid
        else:
            url_id = data[0]
            cursor.execute('SELECT hash_id FROM hash_table WHERE url_id = (?)', (url_id,))
            data = cursor.fetchone()
            hash_id = data[0]
            short_url = request.host_url + hash_id

        conn.commit()
        conn.close()

        msg = 'Success'
        body = short_url
        return response(body = body, msg = msg), 200

