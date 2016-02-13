from flask import Flask
from flask import render_template
from LayoutGenerator import *
import DisplayLoader

app = Flask(__name__)

@app.route("/")
def hello():
    displays = DisplayLoader.loadDisplays()
    panels = []
    for display in displays:
        panels.append(LayoutGenerator.htmlForDisplay(display))
    return render_template("index.html", displays=panels)

if __name__ == "__main__":
    app.run(debug=True)
