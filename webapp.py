from flask import Flask, request, Markup, render_template
import os
import json
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':    
    app.run(debug=False)
        
