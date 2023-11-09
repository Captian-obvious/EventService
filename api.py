#Modules & Flaak
import errors,os,sys,requests,robloxapi
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
#Server stuff
def getParams(url):
    if (len(url.split('?'))>1):
        query=url.split('?')[1]
        params=query.split('&')
        return params
    ##endif
##end

class eventserver:
    Schedules=[]
    def createSchedule(name):
        class newSchedule:
            Name=name
            Events=[]
            def append(data):
                if (data!=None):
                    newSchedule.Events.append(data)
                else:
                    eventserver.error("'data' was null!")
                ##endif
            ##end
            def addEvent(name,weight,script):
                if (name!=None):
                    weight=weight || 0
                    script=script || None
                    if (script!=None):
                        class data:
                            Name=name
                            Weight=weight
                            Script=script
                        ##end
                        newSchedule.append(data)
                        return data
                    else:
                        eventserver.error("You must provide a valid JSON Value for property 'SourceScript'!")
                    ##endif
                else:
                    eventserver.error("You must provide a valid JSON Value for property 'Name'!")
                ##endif
            ##end
            def getEventFromName(name):
                evs=newSchedule.Events
                ret=None
                if (len(evs)>0):
                    for i in range(evs):
                        if (evs[i] and evs[i].Name==name):
                            break
                            ret = evs[i]
                        ##endif
                    ##end
                ##endif
                return ret
            ##end
        ##end
        eventserver.Schedules.append(newSchedule)
        return newSchedule
    ##end
    def getScheduleFromName(name):
        sched=eventserver.Schedules
        ret=None
        if (len(sched)>0):
            for i in range(len(sched)):
                if (sched[i] and sched[i].Name==name):
                    break
                    ret=sched[i]
                ##endif
            ##end
        ##endif
        return ret
    ##end
    def error(err,errString):
        if (err!=None and errString!=None):
            errMsg={
                "ErrorCode": errors.getErrorCodeFromString(errString),
                "ErrorMessage":err,
                "CompletedStatus":False,
            }
            return jsonify(errMsg)
    ##end
##end
