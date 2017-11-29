
from locust import HttpLocust, TaskSet, task
#import requests


class locustLoad(TaskSet):

    @task(1)
    def index(self):
        self.client.get("/")


class sampleLoadTest(TaskSet):

    @task(1)
    def UserCredentials(self):
            response = self.client.request(method="POST",
                                           url="url/endpoint",
                                           headers={
                                               'content-type': "application/x-www-form-urlencoded",
                                               'authorization': "HASH",
                                               'channel': "WEB/Mobile",
                                               'client-version': "something",
                                               'user-agent': "x2b6ZreHt38MpteUHQ33",
                                               'device-name': "IPhone 10",
                                               'cache-control': "no-cache",
                                               'postman-token': "fb625ab1-efe6-be3e-481b-3064a83eef6b"
                                           },
                                           data={
                                               'some data': "something"
                                           }
                                           )

            #response = requests.request("POST", url, data=payload, headers=headers)

            print(response.status_code)

    @task(2)
    def UserProfile(self):
        response = self.client.request(method="GET",
                                       url="url/enpoint",
                                       headers={
                                           'authorization': "HASH",
                                           'channel': "MOBILE/Web",
                                           'client-version': "something",
                                           'guest-mode': "false",
                                           'cache-control': "no-cache",
                                           'postman-token': "ae04ca49-2371-2234-1fbe-a6131157a515",
                                           'user-agent': "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0"
                                           #adding a user-agent allows you to not get 'Connection aborted.', BadStatusLine("''",)
                                       },
                                       )

        print(response.text)


class LoadTestApi(HttpLocust):
        #host = 'some-host'
    task_set = sampleLoadTest
    min_wait = 5000
    max_wait = 9000
