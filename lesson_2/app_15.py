from flask import Flask, request, make_response, redirect, url_for, flash, render_template

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'

@app.route('/', methods=['GET', 'POST'])
@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Проверка данных формы
        if not request.form['name']:
            flash('Введите имя!', 'warning')
            return redirect(url_for('form'))
        elif len(request.form['name'].strip()) < 1:
            flash("Неверное имя", 'danger')
            return redirect(url_for('form'))
        
        # Обработка данных формы
        response = make_response(redirect(url_for('form')))
        response.set_cookie('username', request.form['name'])
        flash('Форма успешно отправлена!', 'success')
        return response

    return render_template('flash_form.html')


@app.route('/get/')
def get_cookies():
# получаем значение cookie
    name = request.cookies.get('username')
    return f"Значение cookie: {name}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)