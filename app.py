from flask import Flask, render_template, request
import os
 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/result.html')
def result():
    num = request.args['shortcode']
    return render_template('result.html', results = exec(num))

if __name__ == "__main__":
    app.run(debug=True)