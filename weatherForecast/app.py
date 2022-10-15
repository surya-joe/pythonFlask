from flask import Flask, render_template, request 
import requests
import json

app = Flask(__name__) 

API_KEY = "e3dc3da840msh029ff60fb38eb47p147d3cjsncb1ccd2d319a"
API_HOST = "weatherapi-com.p.rapidapi.com"
API_URL = "https://weatherapi-com.p.rapidapi.com/current.json"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather_report', methods=['GET','POST'])
def predictWeather():
    if request.method == 'POST':
        userInput = request.form['cityName']
        url = API_URL
        query = { 'q':userInput }
        headers = {
            "X-RapidAPI-Key" : API_KEY,
            "X-RapidAPI-Host" : API_HOST
        }
        # print(userInput)
        try:
            response = requests.request("GET", url, headers=headers, params=query)
            jsonData = json.loads(response.text)

            name = jsonData['location']['name']
            temp_c = jsonData['current']['temp_c']
            temp_f = jsonData['current']['temp_f']
            last_update = jsonData['current']['last_updated']
            timeZone = jsonData['location']['tz_id']
            localTime = jsonData['location']['localtime']
            condition_text = jsonData['current']['condition']['text']
            condition_icon = jsonData['current']['condition']['icon']
            windKph = jsonData['current']['wind_kph']

            return render_template('index.html',
                name = name,
                temp_c = temp_c,
                temp_f = temp_f,
                last_update = last_update,
                localTime = localTime,
                timeZone = timeZone,
                condition_text = condition_text,
                condition_icon = condition_icon,
                windKph = windKph
            )
        except:
            return  render_template('index.html', error='Please enter a valid name.')



if __name__ == ('__main__'):
    app.run(debug=True)

