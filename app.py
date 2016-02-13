from flask import Flask
from flask import render_template
import DisplayLoader
import LayoutGenerator

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/ajax/update")
def updater():
    displays = DisplayLoader.loadDisplays()
    panels = []
    for display in displays:
        panels.append(LayoutGenerator.htmlForDisplay(display))
    return render_template("contents.html", displays=panels)

if __name__ == "__main__":
    app.run(debug=True)
