"""

@author: lingw
@email: gw.lin@hzgosun.com
@file: demo.py
@time: 2020-6-2 上午 9:02

I'm a green hand
"""

import itchat
from collections import Counter
import matplotlib.pyplot as plt
import faceapi

# 扫描二维码登陆
itchat.auto_login(hotReload=False)
# 获取好友列表信息
firends = itchat.get_friends(update=True)

def analyseSex(friends):
    sexs = list(map(lambda x:x['Sex'], friends[1:]))
    counts = list(map(lambda x:x[1], Counter(sexs).items()))
    labels = ['Unknow','Male','Female']
    colors = ['red','yellowgreen','lightskyblue']
    plt.figure(figsize=(8,5),dpi=80)
    plt.axes(aspect=1)
    plt.pie(
        counts,  # 性别统计结果
        labels=labels,  # 性别展示标签
        colors=colors,  # 饼图区域配色
        labeldistance=1.1,  # 标签距离圆点距离
        autopct='%3.1f%%',  # 饼图区域文本格式
        shadow=False,  # 饼图是否显示阴影
        startangle=90,  # 饼图起始角度
        pctdistance=0.6  # 饼图区域文本距离圆点距离
            )
    plt.legend(loc='upper right')
    plt.title("{}的微信好友组成".format(friends[0]['Nickname']))
    plt.show()
