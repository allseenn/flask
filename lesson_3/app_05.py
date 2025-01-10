from models_05 import app

@app.route('/')
def index():
    return 'Hi!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5500)