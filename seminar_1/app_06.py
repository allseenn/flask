from flask import Flask, render_template

app = Flask(__name__)

@app.route("/students/")
def students():
    context = {
        'students': [
            ["Иван", "Иванов", 18, 5],
            ["Петр", "Петров", 19, 4],
            ["Сидор", "Сидоров", 20, 3],
        ]
    }
    return render_template('students.html', **context)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5500, debug=True)
