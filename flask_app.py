import time
from flask import Flask
from tasks import compute_fibanocci


app = Flask(__name__)

@app.get("/io")
def io_bound_task():
    time.sleep(1)
    return {"task": "io_bound"}

@app.get("/cpu")
def cpu_bound_task():
    compute_fibanocci(32)
    return {"task": "cpu_bound"}


@app.get("/io_and_cpu")
def mixed_task():
    time.sleep(1)
    compute_fibanocci(32)
    return {"task": "io_and_cpu_bound"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)