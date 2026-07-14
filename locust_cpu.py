from locust import HttpUser, task, constant

class CPUUser(HttpUser):
    wait_time = constant(0)
    @task
    def cpu(self):
        self.client.get("/cpu")
