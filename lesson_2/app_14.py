from flask import Flask, request, make_response, render_template

app = Flask(__name__)
@app.route('/')
def index():
    context = {
        'title': 'Главная',
        'name': 'XapiToN'
    }
    response = make_response(render_template('main.html', **context))
    response.headers['new_head'] = 'New value'
    response.set_cookie('username', context['name'])
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)