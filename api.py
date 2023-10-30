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
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
        <div></div>
    </body>
</html>
"""
##end
