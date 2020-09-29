from datetime import datetime

import requests, time, json, threading, random
from requests import Session

token=["275c4436-d9d3-40e2-847d-bbcf66200043",
"b819c1ba-d14b-4570-a12f-f7a90fe88f98",
"034cf9ad-b18c-4e3e-a9ab-f61792db9742",
"d2b9f7c2-8dc2-4fc1-93b6-90ff16456256"]


def run():
    # self.login_url = login_url




    requests.session = []
    #self.press_url = press_url
    # self.phone = phone
    # self.password = password
    for i in range(token):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Content-Type': 'application/json; charset=UTF-8',

        }
        requests.session.append(Session())
        requests.session[i].headers = requests.headers.copy()
        requests.session[i].headers["x-weimai-token"] = token[i]
        print(run().headers)

    if __name__ == '__main__':
        run()