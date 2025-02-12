from flask import Flask, render_template, request
import json as js
from authLogin import authLogin
from authCreate import authCreate
from money import monthlyIncome
from weather import get_weather_forecast

app = Flask(__name__)


# Main page loading
@app.route('/') 
def home(): 
    return render_template("login.html")

@app.route('/login') 
def login(): 
    return render_template("login.html")

@app.route('/create') 
def create(): 
    return render_template("create.html")

# User Login
@app.route('/logn', methods=['POST'])
def logn():
    name = request.form['name']
    password = request.form['password']
    if authLogin(name, password):
        income, profit, gain = monthlyIncome(name)
        weatherData = get_weather_forecast()
        return render_template("home.html", name=name, income=income, profit=profit, gain=gain, weatherData = weatherData)
    return render_template("login.html")



@app.route('/creat', methods=['POST'])
def creat():
    name = str(request.form['name'])
    password = str(request.form['password'])
    if authCreate(name, password):
        return render_template("login.html")
    return render_template("create.html")










if __name__ == '__main__':
    app.run(debug=True)