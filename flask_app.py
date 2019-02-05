from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")

@app.route('/spaceport', methods=['GET'])
def mainspace():
    return render_template("error.html")