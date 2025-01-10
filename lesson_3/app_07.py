from flask import render_template
from models_06 import app, User

@app.route('/')
def index():
    return 'Hi!'

@app.route('/users/')
def all_users():
    users = User.query.all()
    context = {'users': users}
    print(context)
    return render_template('users.html', **context)

@app.route('/users/<username>/')
def users_by_username(username):
    users = User.query.filter(User.username == username).all()
    context = {'users': users}
    return render_template('users.html', **context)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)
