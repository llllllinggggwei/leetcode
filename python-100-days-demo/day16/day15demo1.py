from socket import socket,SOCK_STREAM,AF_INET
from datetime import datetime

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']
scores = [[None]* len(courses) for _ in range(len(names))]
for row,name in enumerate(names):
    for col,course in enumerate(courses):
        scores[row][col] = float(input(f'{name}的课程{course}分数为:'))
        print(scores)