import requests

url = 'http://127.0.0.1:5000/'
myInp = {
    'num1':2,
    'num2':9
}
x = requests.post(url, json = myInp)
print(x.text)