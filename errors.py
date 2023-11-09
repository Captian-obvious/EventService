#Modules&Flask
import os,requests,robloxapi,sys,time
from api import app,jsonify,request
#class errors
def getErrorCodeFromString(string):
    errCode=None
    if (string=='prop_invalid'):
        errCode=271
    ##endif
    return errCode
##end
