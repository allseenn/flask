from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hi!"

@app.route("/index/")
def html_index():
    context = {
        'title': 'Personal blog',
        'name': 'Hariton'
    }

    return render_template('index2.html', **context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)