from flask import Flask

# An instance of the Flask class is a WSGI application
app = Flask(__name__) 

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/profile/<username>')
def profile(username):
    return "Welcome to {u}'s profile".format(u=username)

@app.route('/add-five/<int:num>')
def add_five(num):
    return "{n} + 6 = {val}".format(n=num, val=num+5)

if __name__ == '__main__':
    #app.run()
    # OR, run for anyone to connect:
    app.run(host='0.0.0.0', debug=True)
