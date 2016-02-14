from flask import Flask
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
    for panel in panels:
        panel.update(delta)
    delta = current_milli_time()
    htmlList = []
    for panel in panels:
        htmlList.append(LayoutGenerator.htmlForDisplay(panel))
    return render_template("contents.html", displays=htmlList)

if __name__ == "__main__":
    app.run(debug=True)
