from crypt import methods
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def sumOfTwoNum():
    num1 = int(request.json['num1'])
    num2 = int(request.json['num2'])
    return f'sum fo {num1} and {num2} is {num1+num2}'

if __name__ == '__main__':
    app.run(debug=True)