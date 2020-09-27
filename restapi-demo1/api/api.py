from flask import Flask, render_template, request , jsonify

app = Flask(__name__)

app.config['DEBUG'] =  True

@app.route('/',methods=['GET'])
def home():
    return render_template("home.html")