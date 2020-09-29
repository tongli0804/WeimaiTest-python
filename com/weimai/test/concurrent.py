#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime

import requests, time, json, threading, random
from requests import Session

token=["275c4436-d9d3-40e2-847d-bbcf66200043",
"b819c1ba-d14b-4570-a12f-f7a90fe88f98",
"034cf9ad-b18c-4e3e-a9ab-f61792db9742",
"d2b9f7c2-8dc2-4fc1-93b6-90ff16456256"]
class concurrent(object):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Content-Type': 'application/json; charset=UTF-8',


    }

    def __init__(self, press_url, phone="1376193000", password="123456"):
        # self.login_url = login_url
        r = requests

        self.session = []
        self.press_url = press_url
        # self.phone = phone
        # self.password = password
        for i in range(THREAD_NUM):
            self.session.append(Session())
            self.session[i].headers = self.headers.copy()
            self.session[i].headers["x-weimai-token"] = token[i]
            print(self.headers)



    # def login(self):
    #     '''登陆获取session'''
    #     data = {"businessType": "string", "couponId": "string"}
    #     res = self.session.post(self.login_url, data=json.dumps(data))
    #     XToken = res.json().get('_educoder_session')
    #     self.session.headers['X-Token'] = XToken

    def testinterface(self, index):
        '''压测接口'''

        #self.session[index].headers['X-UnionId'] = 'of6uw1CUVhP533sQok'
        data = {"businessType": 320, "couponId": 1595038795969900545}
        html = self.session[index].post(self.press_url, data=json.dumps(data).encode(encoding='utf-8'))
        #r = requests[index].post(self.press_url, data=json.dumps(data).encode(encoding='utf-8'))
        global ERROR_NUM
        try:
            if html.json().get('code') != 0:
                print("错误内容"+html.json())
                ERROR_NUM += 1
        except Exception as e:
            print(e)
            ERROR_NUM += 1

    def testonework(self, index):
        '''一次并发处理单个任务'''
        i = 0
        while i < ONE_WORKER_NUM:
            i += 1
            self.testinterface(index)
        # time.sleep(LOOP_SLEEP)

    def run(self):
        '''使用多线程进程并发测试'''
        dt = datetime.now()

        t1 = time.time()
        Threads = []

        for i in range(THREAD_NUM):

            t = threading.Thread(target=self.testonework(i), name="T" + str(i))
            t.setDaemon(True)
            Threads.append(t)

        for t in Threads:
            t.start()
            #print(dt)
            #print(str(dt) +" " + t.name )
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

    press_url = 'http://integration.myweimai.com/activitycenter/api/activity/seckill/seckillcoupon?channelAlias=&channelSource=&channelPlatform=103'
    THREAD_NUM = 4  # 并发线程总数
    ONE_WORKER_NUM = 1  # 每个线程的循环次数
    # LOOP_SLEEP = 0.1  # 每次请求时间间隔(秒)
    ERROR_NUM = 0  # 出错数

    obj = concurrent(press_url=press_url)
    # obj.login()
    obj.run()