Flask Tutorial (mempy)
======================

A simple introduction to `Flask <http://flask.pocoo.org/docs/quickstart/>`_

Installation::

    pip install flask

Hello World
-----------

A simple hello world app (``hello.py``)::

    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run()

Run the server::
    
    python hello.py

Now, run in Debug Mode, and allow anyone on the network to connect::

    app.run(host='0.0.0.0', debug=True)

Add a new/different route and function/page::
        
    @app.route('/profile/<username>')
    def profile(username):
        return "Welcome to {u}'s profile".format(u=username)

Add a converter for variable parameters in the URL::

    @app.route('/add-five/<int:num>')
    def add_five(num):
        return "{n} + 6 = {val}".format(n=num, val=num+5)


A Guestbook
-----------

OR, *Welcome to 1997*.


Create the directory structure::

    /guestbook
        /templates

We'll put our application in the ``guestbook`` directory, and we'll write some
HTML templates (using `Jinja2 <http://jinja.pocoo.org/docs/templates/>`_), which
go in the ``templates`` directory.


