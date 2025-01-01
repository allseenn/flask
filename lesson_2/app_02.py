from flask import Flask, url_for

app = Flask(__name__)

@app.route('/test_url_for/<int:num>/')
def test_url(num):
    text = f'В num лежит {num}<br>'
    text += f'Функция {url_for("test_url", num=num) = }<br>'
    text += f'Функция {url_for("test_url", num=num, data="new_data") = }<br>'
    text += f'Функция {url_for("test_url", num=num, data="new_data", pi=3.14515) = }<br>'
    return text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5500, debug=True)