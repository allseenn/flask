import logging
from flask import Flask, render_template, request, abort, redirect, url_for
# from lesson_2.db import get_blog

app = Flask(__name__)
logger = logging.getLogger(__name__)

context = {'title': 'Новости',
            'news': 'Новости',
            'main': 'Главная',
            'data': 'База статей'}


@app.route('/internal/')
def internal():
    return redirect(url_for('main'))


@app.route('/external/')
def external():
    return redirect(('https://google.com'))

@app.route('/news/')
def news():
    return render_template('news.html', **context)

@app.route('/main/')
def main():
    context['title'] = 'Главная'
    return render_template('new_main.html', **context)

@app.route('/data/')
def data():
    context['title'] = 'Статьи'
    return render_template('new_data.html', **context)


@app.errorhandler(404)
def page_not_found(e):
    logger.warning(e)
    context['title'] = 'Страница не найдена'
    context['url'] = request.base_url
    return render_template('404.html', **context), 404

@app.errorhandler(500)
def page_not_found(e):
    logger.error(e)
    context['title'] = 'Ошибка сервера'
    context['url'] = request.base_url
    return render_template('500.html', **context), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)