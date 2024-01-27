from flask import Flask, render_template
import math
app = Flask(__name__)
import os


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))


#bruh moment