from flask import Flask, render_template

app = Flask(__name__)

@app.route('/news/')
def news():
    context = {'title': 'Новости',
               'news': 'Новости',
               'main': 'Главная',
               'data': 'База статей'}
    return render_template('news.html', **context)

@app.route('/main/')
def main():
    context = {'title': 'Главная',
               'news': 'Новости',
               'main': 'Главная',
               'data': 'База статей'}
    return render_template('new_main.html', **context)

@app.route('/data/')
def data():
    context = {'title': 'База статей',
               'news': 'Новости',
               'main': 'Главная',
               'data': 'База статей'}
    return render_template('new_data.html', **context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)