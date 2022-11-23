"""
Space Butterflies: Gordon Mo, Harry Zhu
Softdev
K20 -- REST API 
2022-11-21
time spent
"""

from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)
<<<<<<< HEAD
=======

key = open("key_nasa.txt").read()
urlString = "https://api.nasa.gov/planetary/apod?api_key=" + key
res = requests.get(urlString)
json = res.json()
#print(res.text) #str type
#print(json["url"])
>>>>>>> 9e8d3ee71eb2def80f93066fadd8f7496a0c3c0c

@app.route("/")
def picture():
    return render_template('main.html', url = json["url"], explanation = json["explanation"], title = json["title"])

with open('key_nasa.txt') as f:
    key = f.read()

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()

