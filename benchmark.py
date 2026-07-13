import subprocess

def run_benchmark(t="2m"):
    for fw in [{"name": "flask", "addr": "http://localhost:3000"}, {"name": "fastapi", "addr": "http://localhost:4000"}]:
        for u in [50, 100, 200, 400, 600, 800]:
            for lt in [{"name": "io", "file": "locust_io.py"}, {"name": "cpu", "file": "locust_cpu.py"}, {"name": "mixed", "file": "locust_mixed.py"}]:
                subprocess.run([
                    "locust", 
                    "--headless",
                    "-u", str(u),
                    "-r", "20",
                    "-t", t,
                    "--csv", f"results/{fw['name']}_{lt['name']}_{u}",
                    "-H", fw['addr'],
                    "-f", lt['file'],
                ], check=True)

if __name__ == "__main__":
    # warmup
    run_benchmark("30s")
    # run benchmark
    run_benchmark()