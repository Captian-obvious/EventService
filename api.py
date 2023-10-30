#Modules & Flaak
import os,sys,requests,robloxapi
from flask import Flask, requests, jsonify
#Define app
app=Flask(__name__)
#Defibe views.

# DYNAMIC PAGES
@app.route('/')
def index():
    page="""
<h1 id='headingText' class='red1 center'>Welcome!</h1>
<h2 class='red2 center'>Welcome to the EventService Landing Page.</h2>
<p class='red1 center'>
    Here you wont exactly find much, but this is The index of the API.<br>
    API pages can be found under <a href='/api/'>/api/</a>.
</p>
"""
    return """
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <div>
            """+page+"""
        </div>
    </body>
</html>
 """
##end
