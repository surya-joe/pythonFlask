from flask import Flask,render_template,flash,request

app = Flask(__name__)
app.secret_key = 'secret key'

@app.route('/')
def index():
    flash("What's your name?")
    return render_template('index.html')

@app.route('/greet', methods=['POST','GET'])
def greet():
    input_name = request.form['nameInput']
    if input_name.strip() != '':
        flash('Hi ' + str(input_name) + ', Great to see you.')
        return render_template('explore.html')
    else:
        flash('Name cann\'t be empty string') 
        return render_template('index.html')

if __name__ == ('__main__'):
    app.run(debug=True)