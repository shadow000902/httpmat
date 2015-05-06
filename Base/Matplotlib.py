__author__ = 'Administrator'
import numpy as np
import matplotlib.pyplot as pl
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题
def autolabel(ax, rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height), ha='center', va='bottom')

#柱形
def  mat_bar(args_list, title='登陆', xtitle='请求数量', ytitle='响应时间'):
    N = len(args_list[0])
    print(N)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, args_list[0], width, color='r')
    #womenMeans = args_list[1]
    #rects2 = ax.bar(ind+width, womenMeans, width, color='y')

    # add some
    ax.set_ylabel(ytitle)
    ax.set_xlabel(xtitle)
    ax.set_title(title)
    ax.set_xticks(ind+width)
    ax.set_xticklabels(args_list[1])

    #ax.legend((rects1[0], rects2[0]), ('Men', 'Women') )
    autolabel(ax, rects1)
    #autolabel(ax, rects2)
    plt.show()

#曲线[1, 2, 3, 4, 5]  [1, 4, 9, 16, 25]
def mat_plot(args_list, title='登陆', xtitle='请求数量', ytitle='响应时间', xlim=20, ylim=3):
    x1 = args_list[0]# Make x, y arrays for each graph
    y1 = args_list[1]
    #x2 = [1, 2, 4, 6, 8]
    #y2 = [2, 4, 8, 12, 16]
    pl.plot(x1, y1, 'r')# use pylab to plot x and y
    #pl.plot(x2, y2, 'g')
    pl.title(title)# give plot a title
    pl.xlabel(xtitle)# make axis labels
    pl.ylabel(ytitle)
    pl.xlim(0.0, int(xlim))
    pl.ylim(0.0, int(ylim))
    pl.show()


 #饼状
def mat_pie(args_list, title="登陆"):
    #list_arg = [['Frogs', 'Hogs', 'Dogs', 'Logs'], ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral'], [15, 30, 45, 10]]
    plt.figure(1, figsize=(6,6))
    pie_sum = []
    pie_title = []
    pie_color = []
    for i in range(len(args_list[2])): #[0 30, 0, 10] 对lsit中包含0的筛选出去
        if args_list[2][i] != 0:
            pie_sum.append(args_list[2][i])
            pie_title.append(args_list[0][i])
            pie_color.append(args_list[1][i])

    labels = pie_title
    sizes = pie_sum
    colors = pie_color
    plt.title(title, loc=u'left')
    #explode = (0, 0, 0, 0.1) # 对应sizes，数值越大就会凸出饼形
    pl.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle.
    pl.axis('equal')
    pl.show()

