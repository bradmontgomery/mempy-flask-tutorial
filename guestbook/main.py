"""
A *really* simple guestbook flask app. Data is stored in a SQLite database that
looks something like the following:

+------------+------------------+------------+ 
| Name       | Email            | signed_on  | 
+============+==================+============+ 
| John Doe   | jdoe@example.com | 2012-05-28 | 
+------------+------------------+------------+ 
| Jane Doe   | jane@example.com | 2012-05-28 | 
+------------+------------------+------------+ 

This can be created with the following SQL (see bottom of this file):

    create table guestbook (name text, email text, signed_on date);

Related Docs:
* `sqlite3 <http://docs.python.org/library/sqlite3.html>`_
* `datetime <http://docs.python.org/library/datetime.html>`_
* `Flask <http://flask.pocoo.org/docs/>`_

"""
from datetime import date
from flask import Flask, redirect, request, url_for, render_template

import sqlite3

app = Flask(__name__)       # our Flask app
DB_FILE = 'guestbook.db'    # file for our Database

def _select():
    """
    just pull all the results from the database
    """
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM guestbook")
    return cursor.fetchall()

def _insert(name, email):
    """
    put a new entry in the database
    """
    params = {'name':name, 'email':email, 'date':date.today()}
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    
    cursor.execute("insert into guestbook (name, email, signed_on) VALUES (:name, :email, :date)", params)

    connection.commit()
    cursor.close()

@app.route('/')
def index():
    """ 
    List everyone who's signed the guestbook 
    
    """
    entries = [dict(name=row[0], email=row[1], signed_on=row[2] ) for row in _select()]
    return render_template('index.html', entries=entries)

@app.route('/sign', methods=['POST'])
def sign():
    """
    Accepts POST requests, and processes the form;
    Redirect to index when completed.
    """
    _insert(request.form['name'], request.form['email']) 
    return redirect(url_for('index'))

if __name__ == '__main__':

    # Make sure our database exists
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    try:
        cursor.execute("select count(rowid) from guestbook")
    except sqlite3.OperationalError:
        cursor.execute("create table guestbook (name text, email text, signed_on date)")
    cursor.close()
        

    app.run(host='0.0.0.0', debug=True)
