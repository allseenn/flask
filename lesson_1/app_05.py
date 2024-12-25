from flask import Flask

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home</title>
</head>
<body>
    <h1>Title</h1>
    <h2>Header</h2>
    <h3>Subheader</h3>
    <p><a href="/text/">Text</a></p>
</body>
</html>
"""

@app.route('/')
def home():
    return html

@app.route('/text/')
def text():
    return """
Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, 
quis nostrud exercitation ullamco 
laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse 
cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non 
proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum.
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500)