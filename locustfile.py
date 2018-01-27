# script used againt vagrant set up on bookshelf git repo
# url to repo: https://github.com/andela-sjames/bookshelf

# tutorial reference: loading ... 

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
    def search_for_book_that_contains_string_space(self):
        self.client.get("/?q=space")

    def search_for_book_that_contains_string_man(self):
        self.client.get("/?q=man")

class WebsiteUser(HttpLocust):
    host = "http://bookshelf.example"
    task_set = SampleTrafficTask
    min_wait = 5000
    max_wait = 9000
