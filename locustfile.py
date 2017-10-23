
from locust import HttpLocust, TaskSet, task
#import requests


class locustLoad(TaskSet):

    @task(1)
    def index(self):
        self.client.get("/")


class stagingLoadTest(TaskSet):

    @task(1)
    def UserCredentials(self):
            response = self.client.request(method="POST",
                                           url="https://api.stg-kudo.com/v3/users/credentials",
                                           headers={
                                               'content-type': "application/x-www-form-urlencoded",
                                               'authorization': "OW9xSHN1ZXBPUklKRDZKWjp0dzNRSDJuMGxiMndmZGhVeENvdGVQNlowc2FRVnp1RA==",
                                               'channel': "MOBILE",
                                               'client-version': "54",
                                               'user-agent': "x2b6ZreHt38MpteUHQ33",
                                               'device-name': "IPhone 10",
                                               'cache-control': "no-cache",
                                               'postman-token': "fb625ab1-efe6-be3e-481b-3064a83eef6b"
                                           },
                                           data={
                                               'credentials': "@4c2af9e1114e9c1bc09b5f17a436bcd16613fa77::4c1b9bb3405f53cf46731af89f07b01d1ffe974f944d81085cb962abc45ee9c3"
                                           }
                                           )

            #response = requests.request("POST", url, data=payload, headers=headers)

            print(response.status_code)

    @task(1)
    def UserProfile(self):
        response = self.client.request(method="GET",
                                       url="https://api.stg-kudo.com/v3/users/profile",
                                       headers={
                                           'authorization': "70MZO4fnOBt7lbqZg63B2a410z6sfkLNfmsICXxo",
                                           'channel': "MOBILE",
                                           'client-version': "54",
                                           'guest-mode': "false",
                                           'cache-control': "no-cache",
                                           'postman-token': "ae04ca49-2371-2234-1fbe-a6131157a515",
                                           'user-agent': "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0"
                                           #adding a user-agent allows you to not get 'Connection aborted.', BadStatusLine("''",)
                                       },
                                       )

        print(response.text)


class LoadTestApi(HttpLocust):
        #host = 'https://api.stg-kudo.com/v3'
    task_set = stagingLoadTest
    min_wait = 5000
    max_wait = 9000
