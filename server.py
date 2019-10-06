from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def create_users():
    theUsername = request.form['username']
    theLocation = request.form['location']
    theLanuage = request.form['language']
    theComment = request.form['comment']
    return render_template("show.html", name=theUsername, dojo=theLocation, favlang=theLanuage, comment=theComment)

if __name__=="__main__":
    app.run(debug=True)