from locust import HttpUser, task, constant

class IOUser(HttpUser):
    wait_time = constant(0)
    @task
    def io(self):
        self.client.get("/io")