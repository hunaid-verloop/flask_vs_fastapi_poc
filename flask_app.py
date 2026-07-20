from flask import Flask
import requests


app = Flask(__name__)

external_api = "http://localhost:6000"

@app.get("/bot")
def bot():
    r = requests.get(external_api)
    return r.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)