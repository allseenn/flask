from flask import Flask

app = Flask(__name__)

@app.route('/number/<float:num>')
def set_number(num):
    print(type(num))
    return f'The number is {num}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)