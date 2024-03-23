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
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10
    return {"station": station,
            "date": date,
            "temperature": temperature}


# run app
if __name__ == "__main__":
    app.run(debug=True)