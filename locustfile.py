import os

from os.path import join, dirname
from dotenv import load_dotenv

from locust import HttpLocust, TaskSet, task

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


email = os.environ.get("email")
password = os.environ.get("password")

class SampleTrafficTask(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        self.client.post("/login", {"email":email, "password":password})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get("/bucketlist/samuel/")

    def single_bucketlist(self):
        self.client.get("/bucketlist/view/49/")

class WebsiteUser(HttpLocust):
    host = "https://moments-bucketlist.herokuapp.com"
    task_set = SampleTrafficTask
    min_wait = 5000
    max_wait = 9000