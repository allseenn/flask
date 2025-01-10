from flask import render_template, jsonify
from models_06 import app, User, Post
from datetime import datetime, timedelta

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

@app.route('/posts/author/<int:user_id>/')
def get_posts_by_author(user_id):
    posts = Post.query.filter_by(author_id=user_id).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})
    

@app.route('/posts/last-week/')
def get_posts_last_week():
    date = datetime.utcnow() - timedelta(days=7)
    posts = Post.query.filter(Post.created_at >= date).all()
    if posts:
        return jsonify([{'id': post.id, 'title': post.title, 'content': post.content, 'created_at': post.created_at} for post in posts])
    else:
        return jsonify({'error': 'Posts not found'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)
