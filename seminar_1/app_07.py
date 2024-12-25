from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello'

@app.route('/news/')
def news():
    news = [
        {'title': 'Siria', 'description': 'Asad was gone', 'date': '09.12.2024'},
        {'title': 'Egypt', 'description': 'Pyramid', 'date': '08.12.2024'},
        {'title': 'Iran', 'description': 'Teheran', 'date': '08.12.2024'}
    ]
        
    return render_template('news.html', news=news)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5500)