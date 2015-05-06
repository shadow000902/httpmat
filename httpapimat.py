__author__ = 'Administrator'
#-*- coding: utf-8 -*-
from Base.Http import http_request
from Base.Threads import base_thread
import Base.Matplotlib as bm
from Base.comm import http_commom
import Base.OperateXml as bo
import time
import matplotlib.backends.backend_tkagg
import tkinter
import tkinter.filedialog
import urllib3
hc = http_commom()
br = bo.read_xml()
http_params = {"list_arg": [], "request_num": [], "response_time": [], "sum_03": 0, "sum_5": 0, "sum_1": 0, "sum_timeout": 0}

def sample_request(index=0):
    h = http_request(base_url=br['baseurl'], http_api=br['httpapi'], method=br['method'], http_params=br['postparams'])
    res = h.request()
    http_params['request_num'].append(index+1)
    if res:
        res = '%.2f'%res
        #print(res)
        http_params['response_time'].append(res)

    else:
        http_params['response_time'].append("0")
    if index == int(br['count']) - 1: #如果循环总数循环结束，进行统计操作
            http_params['list_arg'].append(http_params['request_num'])
            http_params['list_arg'].append(http_params['response_time'])
            #print(hc.list_arg)
            if br['mat'] == "plot":
                bm.mat_plot(http_params['list_arg'], title=br["title"], xtitle=br["xtitle"], ytitle=br["ytitle"], xlim=br["xlim"], ylim=br["ylim"])
            elif br['mat'] == "bar":
                bm.mat_bar(http_params['list_arg'], title=br["title"], xtitle=br["xtitle"], ytitle=br["ytitle"])
            elif br['mat'] == 'pie':
                for j in http_params['list_arg'][1]:
                    temp = float(j)
                    # print(temp)
                    if temp < 0.30 and temp != 0.0:
                        http_params['sum_03'] += 1
                    if temp >= 0.30 and temp < 1.00:
                        http_params['sum_1'] += 1
                    if temp >= 1.00 and temp < 5.00:
                        http_params['sum_5'] += 1
                    if temp == 0:
                         http_params['sum_timeout'] += 1

                sum1 = float((http_params['sum_1']/int(br["count"]))*100)
                sum03 = float((http_params['sum_03']/int(br["count"]))*100)
                sum5 = float((http_params['sum_5']/int(br["count"]))*100)
                sum_timeout = float((http_params['sum_timeout']/int(br["count"]))*100)
                list_arg = None
                if (int(br["count"])) == (http_params['sum_1'] + http_params['sum_03'] + http_params['sum_5'] + http_params['sum_timeout']):
                    list_arg = [[u'小于300ms请求共:' + str(http_params['sum_03'])+'个', u'300-1000ms请求共:' + str(http_params['sum_1'])+'个',
                                 u'1s-5s 请求共:'+str(http_params['sum_5'])+'个', u'请求超时共:'+str(http_params['sum_timeout'])+'个'], ['yellowgreen', 'gold', 'lightskyblue', 'red'], [sum03, sum1,sum5, sum_timeout]]
                else:
                    sumother =int(br["count"]) - (http_params['sum_1'] + http_params['sum_03'] + http_params['sum_5'] + http_params['sum_timeout'])
                    sum_o = 0
                    if sumother!= 0:
                        sum_o = (sumother/int(br["count"]))*100
                    list_arg = [[u'小于300ms请求共:' + str(http_params['sum_03']) + '个', u'300-1000ms请求共:' + str(http_params['sum_1']) + '个',
                                 '1s-5s 请求共:'+str(http_params['sum_5']) + '个', u'大于5s请求共:'+str(sumother) + '个', u'请求超时共:'+str(http_params['sum_timeout'])+'个'], ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red'], [sum03, sum1, sum5, sum_o, sum_timeout]]
                print(list_arg)
                bm.mat_pie(list_arg, title=br["title"])
def multi_thread():
    threads = []
    for i in range(0, int(br["count"])):
        threads.append(base_thread(sample_request(index=i)))
    for j in range(0, int(br["count"])):
        threads[j].start()
    for k in range(0, int(br["count"])):
        threads[k].join()


multi_thread()
