import time
from flask import Flask
from tasks import compute_fibanocci


app = Flask(__name__)

@app.get("/io_bound")
def io_bound_task():
    time.sleep(1)
    return {"task": "iobound"}

@app.get("/cpu_bound")
def cpu_bound_task():
    compute_fibanocci(32)
    return {"task": "cpu_bound"}


@app.get("/io_and_cpu")
def mixed_task():
    time.sleep(1)
    compute_fibanocci(32)
    return {"task": "mixed"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)