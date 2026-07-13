from locust import HttpUser, task, constant

class MixedUser(HttpUser):
    wait_time = constant(0)
    @task
    def mixed(self):
        self.client.get("/io_and_cpu")
