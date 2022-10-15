import requests

# url = 'http://127.0.0.1:5000/'
myInp = {
    'num1':2,
    'num2':7
}
x = requests.post('http://127.0.0.1:5000/', json = myInp)
print(x.text)