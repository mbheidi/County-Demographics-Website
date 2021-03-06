from flask import Flask, request, Markup, render_template
import os
import json
app = Flask(__name__)

@app.route('/')
def home():
    with open('classics.json') as classics_data:
        data = json.load(classics_data)
    options=""
    for d in data:
        author=d['bibliography']['author']['name']
        options += Markup("<option value=\"" + author + "\">" + author + "</option>")
    return render_template('author.html', options=options)

@app.route("/p1")
def render_page1():
    return render_template('index.html')

@app.route("/p2")
def render_page2():
    return render_template('subject.html')

@app.route("/p3")
def render_page3():
    return render_template('title.html')

@app.route("/p4")
def render_page4():
    return render_template('year.html')

@app.route("/response")
def render_response():
    author = request.args['author'] 
    with open('classics.json') as classics_data:
        data = json.load(classics_data)
    return render_template('response.html', response = author)
    for myVariable in data:

if __name__ == '__main__':    
    app.run(debug=False)
      
