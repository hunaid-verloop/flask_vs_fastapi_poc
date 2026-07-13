from locust import HttpUser, task, constant


class IOUser(HttpUser):
    wait_time = constant(0)
    @task
    def io(self):
        with self.client.get("/io_bound", catch_response=True) as response:
            if response.elapsed.total_seconds() > 2:
                response.failure("Too slow")


class CPUUser(HttpUser):
    wait_time = constant(0)
    @task
    def cpu(self):
        self.client.get("/cpu_bound")


class MixedUser(HttpUser):
    wait_time = constant(0)
    @task
    def mixed(self):
        self.client.get("/io_and_cpu")
