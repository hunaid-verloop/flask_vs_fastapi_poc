from locust import HttpUser, task, constant


class BotUser(HttpUser):
    wait_time = constant(0)
    @task
    def bot(self):
        self.client.get("/bot")

