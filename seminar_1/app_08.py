from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    title = 'Main'
    news = [
        {'title': 'Siria', 'description': 'Asad was gone', 'date': '09.12.2024'},
        {'title': 'Egypt', 'description': 'Pyramid', 'date': '08.12.2024'},
        {'title': 'Iran', 'description': 'Teheran', 'date': '08.12.2024'}
    ]
    return render_template('main.html', title=title, news=news)

@app.route('/about/')
def about():
    title = 'About'
    return render_template('about.html', title=title)

@app.route('/contacts/')
def contacts():
    title = 'Contacts'
    return render_template('contacts.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)