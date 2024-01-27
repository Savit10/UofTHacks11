from flask import Flask, request, render_template, redirect, url_for

# Flask constructor
app = Flask(__name__, template_folder="templates")   
# A decorator used to tell the application
# which URL is associated function

output = [{"input": "Sample input", "output": "Sample output"}]

@app.route("/")

def index():
    return render_template("index.html", output=output)

@app.route('/spongebob')
def spongebob():
    return render_template('spongebob.html')

@app.route('/sandy')
def sandy():
    return render_template('sandy.html')

@app.route('/patricks')
def patricks():
    return render_template('patricks.html')
        
@app.route('/', methods =["GET", "POST"])
def newinputoutput():
    if request.method == "POST":
       input = request.form.get("user-input") 
       output.append(input, input)
       return redirect(url_for("index"))
    return render_template("spongebob.html")



if __name__ == '__main__':
    app.run(debug=True)