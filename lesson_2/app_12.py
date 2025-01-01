
import logging
from flask import Flask, render_template, request, abort, redirect, url_for

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return f'Привет, {name}!'
    
@app.route('/redirect/<name>')
def redirect_to_hello(name):
    return redirect(url_for('hello', name=name))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)