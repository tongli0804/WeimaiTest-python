#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests, time, json, threading, random
from requests import Session

token=["_educoder_session=e62599e274fddbe7a2a178317b666e1d; autologin_trustie=8aa6b387bb358ec12c9ac148aa08b4e10b0b689e;","autologin_trustie=8aa6b387bb358ec12c9ac148aa08b4e10b0b689e; _educoder_session=350d0ea28b9a0702bebc5a75b3012cfe"]
class concurrent(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',
    }

    def __init__(self, login_url, press_url, phone="1376193000", password="123456"):
        # self.login_url = login_url
        self.session = []
        self.press_url = press_url
        # self.phone = phone
        # self.password = password
        for i in range(THREAD_NUM):
            self.session.append(Session())
            self.session[i].headers = self.headers.copy()
            self.session[i].headers["Cookie"] = token[i]


    def login(self):
        '''登陆获取session'''
        data = data = {'t': int(time.time() * 1000), 'login': self.phone, 'password': self.password}
        res = self.session.post(self.login_url, data=json.dumps(data))
        XToken = res.json().get('_educoder_session')
        self.session.headers['X-Token'] = XToken

    def testinterface(self,index):
        '''压测接口'''
        self.session[index].headers['X-UnionId'] = 'of6uw1CUVhP533sQok'
        data = {}
        global ERROR_NUM
        try:
            html = self.session[index].get(self.press_url, data=json.dumps(data))
            # if html.json().get('code') != 0:
            print(html.json())
                # ERROR_NUM += 1
        except Exception as e:
            print(e)
            ERROR_NUM += 1

    def testonework(self,index):
        '''一次并发处理单个任务'''
        i = 0
        while i < ONE_WORKER_NUM:
            i += 1
            self.testinterface(index)
        # time.sleep(LOOP_SLEEP)

    def run(self):
        '''使用多线程进程并发测试'''
        t1 = time.time()
        Threads = []

        for i in range(THREAD_NUM):
            t = threading.Thread(target=self.testonework(i), name="T" + str(i))
            t.setDaemon(True)
            Threads.append(t)

        for t in Threads:
            t.start()
        for t in Threads:
            t.join()
        t2 = time.time()

        print("===============压测结果===================")
        print("URL:", self.press_url)
        print("任务数量:", THREAD_NUM, "*", ONE_WORKER_NUM, "=", THREAD_NUM * ONE_WORKER_NUM)
        print("总耗时(秒):", t2 - t1)
        print("每次请求耗时(秒):", (t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM))
        print("每秒承载请求数:", 1 / ((t2 - t1) / (THREAD_NUM * ONE_WORKER_NUM)))
        print("错误数量:", ERROR_NUM)


if __name__ == '__main__':
    login_url = 'https://www.educoder.net/api/accounts/login.json'
    press_url = 'https://www.educoder.net/api/users/get_user_info.json?school=1'
    phone = "kosasa01"
    password = "kosasa33!"

    THREAD_NUM = 2  # 并发线程总数
    ONE_WORKER_NUM = 1  # 每个线程的循环次数
    # LOOP_SLEEP = 0.1  # 每次请求时间间隔(秒)
    ERROR_NUM = 0  # 出错数

    obj = concurrent(login_url=login_url, press_url=press_url, phone=phone, password=password)
    # obj.login()
    obj.run()