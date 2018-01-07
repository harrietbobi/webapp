from flask import Flask, render_template
# initializing the application instance
app = Flask(__name__)
# handling routes
@app.route('/')
def create():
    return render_template('create.html')
# # creates a dynamic route
# @app.route('/signin/<name>')
# def signin(name):
#     return render_template('signin.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)