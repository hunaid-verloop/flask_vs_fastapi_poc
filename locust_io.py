from locust import HttpUser, task, constant

class IOUser(HttpUser):
    wait_time = constant(0)
    @task
    def io(self):
        with self.client.get("/io_bound", catch_response=True) as response:
            if response.elapsed.total_seconds() > 2:
                response.failure("Too slow")