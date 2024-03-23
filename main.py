import pandas as pd
from flask import Flask, render_template

# create the website object
app = Flask(__name__)


# default page template
@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def data(station, date):
    temperature = 23
    return {"station": station,
            "date": date,
            "temperature": temperature}


# run app
if __name__ == "__main__":
    app.run(debug=True)