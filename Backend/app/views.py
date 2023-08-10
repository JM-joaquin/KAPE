from flask import render_template
from run import app

url = "http://127.0.0.1:3000"

@app.route('/')
def Index():
    return render_template('index.html')