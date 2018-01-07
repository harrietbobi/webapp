from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup")
def signup():
     
    return render_template("signup.html")


@app.route("/signin")
def signin():
      
    return render_template("signin.html")


@app.route("/view")
def view():
      
    return render_template("view.html")
@app.route("/create")
def create():
      
    return render_template("create.html")
@app.route("/update")
def update():
      
    return render_template("update.html")
@app.route("/delete")
def delete():
      
    return render_template("create.html")
@app.route("/logout")
def logout():
      
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
