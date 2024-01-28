from flask import Flask, request, render_template, redirect, url_for, session
from cohereaifile import get_response
import atexit
import os
# Flask constructor
app = Flask(__name__, template_folder="templates")  
app.secret_key = os.urandom(24) 
# A decorator used to tell the application
# which URL is associated function

outputSpongebob = []
outputSandy = []
outputPatrick = []
output = []

@app.route("/")

def index():
    return render_template("index.html", output=output)

@app.route('/spongebob', methods=["GET", "POST"])
def spongebob():
    if request.method == "POST":
        input = request.form.get("user-input")
        screenOutput = get_response(input, "SpongeBob")
        session['outputSpongebob'] = {"input": input, "screenOutput": screenOutput}
        return render_template('spongebob.html', output=session['outputSpongebob'])
    return render_template('spongebob.html')

@app.route('/sandy', methods=["GET", "POST"])
def sandy():
    if request.method == "POST":
        input = request.form.get("user-input")
        screenOutput = get_response(input, "Sandy")
        session['outputSandy'] = {"input": input, "screenOutput": screenOutput}
        return render_template('sandy.html', output=session['outputSandy'])
    return render_template('sandy.html')

@app.route('/patricks', methods=["GET", "POST"])
def patricks():
    if request.method == "POST":
        input = request.form.get("user-input")
        screenOutput = get_response(input, "Patrick")
        session['outputPatrick'] = {"input": input, "screenOutput": screenOutput}
        return render_template('patricks.html', output=session['outputPatrick'])
    return render_template('patricks.html')

if __name__ == '__main__':
    def clear_lists():
        outputSpongebob.clear()
        outputSandy.clear()
        outputPatrick.clear()
        output.clear()

    atexit.register(clear_lists) 

    app.run(debug=True)

