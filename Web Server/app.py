from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
from time import sleep
import time
import subprocess



app = Flask(__name__)

@app.route('/')

def index():
    templateData = {
        'image' : '/static/image.jpg',
        'route' : '/opening',
        'button-text' : 'unlock'
    }
    return render_template('index.html', **templateData)

@app.route("/opening")

def runmotor():
    subprocess.call("sudo python static/servo4.py", shell = True)
    templateData = {
        'image' : '/static/image.jpg',
        'route' : '/closing',
        'button-text' : 'unlock'
    }
    return render_template('index.html', **templateData)

@app.route("/closing")

def closemotor():
    subprocess.call("sudo python static/servo3.py", shell = True)
    templateData = {
        'image' : '/static/image.jpg',
        'route' : '/opening',
        'button-text' : 'lock'
    }
    return render_template('index.html', **templateData)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
