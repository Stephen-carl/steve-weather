#this is the default file for the application
#a flask instance will be running our application

from flask import Flask, render_template, request
from weather import getCurrentWeather
#to serve our application to the server
from waitress import serve

#to make our app a flask instance

app = Flask(__name__)
#to define routes, just as i do in node.js using express.ROuter to define routes

@app.route('/')
#define a fumction that will return something for the routes
@app.route('/index')
def index():
    #this will display the html file when the app is running
    return render_template('index.html')
    #return render_template('templates/index.html')

#def route for weather
@app.route('/weather')
def getWeather():
    #city value
    city = request.args.get('city')
    #we need to make sure the city input is not an empty string or string with only spaces
    if not bool(city.strip()):
        city = "Lagos"
    #get the function needed to get the weather
    weather = getCurrentWeather(city)

    #just incase the city is not found or tyhe user put an odd city
    if not weather['cod'] == 200:
        return render_template('city-not-found.html')
    #this will display the html file when the app is running
    return render_template(
        'weather.html',
        #passing the weather data to the html file
        title = weather["name"],
        status = weather["weather"][0]["description"].capitalize(),
        temp =f"{weather["main"]["temp"]:.1f}" ,
        feels_like= f"{weather["main"]["feels_like"]:.1f}"
        )

if __name__ == '__main__':
    #to define the host, which is local host for us
    serve(app, host='0.0.0.0', port=8000)