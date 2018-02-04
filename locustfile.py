# script used against vagrant set up on bookshelf git repo
# url to repo: https://github.com/andela-sjames/bookshelf

from locust import HttpLocust, TaskSet, task

class SampleTrafficTask(TaskSet):

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
