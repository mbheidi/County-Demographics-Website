from flask import Flask, request, Markup, render_template
import os
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')

@app.route("/p2")
def render_page2():
    return render_template('page2.html')

if __name__ == '__main__':    
    app.run(debug=False)
        
