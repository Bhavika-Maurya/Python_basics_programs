from flask import Flask
app= Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'

@app.route('/product')
def products():
    return 'this is a product page'

if __name__ == "__main__":
    app.run(debug=True, port=8000)