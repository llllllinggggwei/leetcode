"""

@author: lingw
@email: gw.lin@hzgosun.com
@file: leetcode_demo.py
@time: 2020-5-18 下午 4:05

I'm a green hand
"""
import itertools
S = "bbbac"
print("".join(str(len(list(v))) for k, v in itertools.groupby(S)))
print(min( S, "".join(k + str(len(list(v))) for k, v in itertools.groupby(S)), key=len))