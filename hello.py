from flask import Flask
# initializing the application instance
app = Flask(__name__)
# handling routes
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
# creates a dynamic route
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    app.run(debug=True)