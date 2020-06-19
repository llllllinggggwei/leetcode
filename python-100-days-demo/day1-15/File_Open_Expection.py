"""

@author: lingw
@email: gw.lin@hzgosun.com
@file: File_Open_Expection.py
@time: 2020-5-20 下午 3:04

I'm a green hand
"""
import json
def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json','w',encoding='utf-8') as fp:
            json.dump(mydict,fp)
    except IOError as e:
        print(e)
    print('over')

if __name__ == '__main__':
    main()