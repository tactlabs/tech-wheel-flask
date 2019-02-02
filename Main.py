from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-wheel', methods=['POST'])
def result():
    
    key1  = request.form.get('key1')
    key2  = request.form.get('key2')
    key3  = request.form.get('key3')
    key4  = request.form.get('key4')
    key5  = request.form.get('key5')
    key6  = request.form.get('key6')
    key7  = request.form.get('key7')
    key8  = request.form.get('key8')
    key9  = request.form.get('key9')
    
    result = {
        'key1' : key1,
        'key2' : key2,
        'key3' : key3,
        'key4' : key4,
        'key5' : key5,
        'key6' : key6,
        'key7' : key7,
        'key8' : key8,
        'key9' : key9,
    }
    
    #return content
    return render_template('result.html', result=result)

def get_parked_place():
    return '288, Spadina Road'

def get_ticket_amount():
    return 45

if __name__ == '__main__':
    host = os.environ.get('IP', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    
    app.run(host= host, port = port, use_reloader = False)
    
    
'''
Sources:
    http://www.compjour.org/lessons/flask-single-page/multiple-dynamic-routes-in-flask/
    
    https://www.learnpython.org/en/String_Formatting
    
    https://stackoverflow.com/questions/25888396/how-to-get-latitude-longitude-with-python
    
    https://github.com/googlemaps/google-maps-services-python
    
    AIzaSyCRhRz_mw_5wIGgF-I6PUy3js6dcY6zQ6Q
    
    Get Current Location:
    https://stackoverflow.com/questions/44218836/python-flask-googlemaps-get-users-current-location-latitude-and-longitude
'''