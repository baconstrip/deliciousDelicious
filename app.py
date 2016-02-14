from flask import Flask
from pprint import pprint
from flask import render_template
from DisplayLoader import * 
import LayoutGenerator

import time

current_milli_time = lambda: int(round(time.time() * 1000))

app = Flask(__name__)
panels = createDisplays()

last = 0

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/ajax/update")
def updater():
    delta = current_milli_time() - last
    statuses = []
    for panel in panels:
        statuses.append(panel.update(delta))
    delta = current_milli_time()
    htmlList = []
    i= 0
    for panel in panels:
        if not statuses[i]:
            statuses[i] = ("Good", 0)
        elif not statuses[i][1]:
            statuses[i][1] = 0
        htmlList.append((statuses[i][0],statuses[i][1],LayoutGenerator.htmlForDisplay(panel)))
        i= i+ 1 
    pprint(statuses)
    return render_template("contents.html", displays=htmlList)

if __name__ == "__main__":
    app.run(debug=True)
