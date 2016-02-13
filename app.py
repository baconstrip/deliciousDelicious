from flask import Flask
from flask import render_template
from DisplayLoader import * 
import LayoutGenerator

app = Flask(__name__)
panels = createDisplays()

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/ajax/update")
def updater():
    htmlList = []
    for panel in panels:
        htmlList.append(LayoutGenerator.htmlForDisplay(panel))
    return render_template("contents.html", displays=htmlList)

if __name__ == "__main__":
    app.run(debug=True)
