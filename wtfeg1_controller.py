"""
wtfeg1_controller: Flask-WTF Example 1 - app controller
"""
import os, binascii
from flask import Flask, render_template, flash, redirect, url_for
from wtfeg1_form import LoginForm

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))  # Flask-WTF: Needed for CSRF

@app.route('/', methods=['get', 'post'])  # First request via GET, subsequent requests via POST
def main():
    form = LoginForm()  # Construct an instance of LoginForm

    if form.validate_on_submit():  # POST request with valid input?
        # Verify username and passwd
        if (form.username.data == 'Peter' and form.passwd.data == 'peter'):
            return redirect(url_for('startapp'))
        else:
            # Using Flask's flash to output an error message
            flash('Wrong username or password')

    # For the initial GET request, and subsequent invalid POST request,
    # render an login page, with the login form instance created
    return render_template('wtfeg1_login.html', form=form)

@app.route('/startapp')
def startapp():
    return 'The app starts here!'

if __name__ == '__main__':
    app.run(debug=True)
