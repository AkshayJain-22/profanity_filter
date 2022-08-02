from flask import Flask, request, render_template, Response
from flask_cors import CORS, cross_origin

import os
app=Flask(__name__)

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

@app.route("/",methods=['GET','POST'])
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)