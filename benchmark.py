import subprocess

TEST_ADDR = "http://localhost:3000"


def run_benchmark(t="2m", test_name="flask"):
    for u in [50, 100, 200]:
        print(f"\n===== Users: {u} =====")
        for lt in [{"type": "io", "file": "locust_io.py"}, {"type": "cpu", "file": "locust_cpu.py"}, {"type": "mixed", "file": "locust_mixed.py"}]:
            print(f"Running {lt['type']}...")
            subprocess.run([
                "locust", 
                "--headless",
                "-u", str(u),
                "-r", "20",
                "-t", t,
                "--csv", f"results/{test_name}_{lt['type']}_{u}",
                "-H", TEST_ADDR,
                "-f", lt['file'],
            ], check=True)
            print("Finished")

if __name__ == "__main__":
    # warmup
    # run_benchmark(t="30s")
    # run benchmark
    run_benchmark()