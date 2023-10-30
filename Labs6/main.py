from flask import request, Flask, render_template
from secret_morse_def import secret_string
import time
app = Flask(__name__)

@app.route('/home', methods = ["POST", "GET"])
def hello_world(*content):
    if request.method == "POST":
        string = request.form['nm']
        return render_template("main.html", content = secret_string(string))
    else: 
        user = "Guest"
        return render_template("main.html", content = "")



