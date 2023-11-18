#Modules&Flask
import os,requests,robloxapi,sys,time
from api import app,jsonify,request
#class errors
def getErrorCodeFromString(string):
    errCode=None
    if (string=='prop_invalid'):
        errCode=271
    elif (string=='access_denied'):
        errCode=273
    elif (string=='method_not_allowed'):
        errCode=274
    elif (string=='resource_not_found'):
        errCode=275
    elif (string=='resource_gone'):
        errCode=276
    elif (string=='unauthenticated'):
        errCode=371
    elif (string=='invalid_assetid'):
        errCode=372
    elif (string=='reserved'):
        errCode=374
    ##endif
    return errCode
##end
