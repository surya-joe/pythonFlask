from ssl import HAS_TLSv1_1
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)
 
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet/<name>')
def greet(name):
    return '<h1>Welcome home %s</h1>' % name
 
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        userInput = request.form['nameInput']
        if userInput != '':
            return redirect(url_for('greet', name=userInput))
        else:
            return render_template('index.html') 
 
if __name__ == '__main__':
    app.run(debug=True)