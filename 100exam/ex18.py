# 100exam 18     求s=a+aa+aaa+aaaa+aa...a的值
from functools import reduce                # 载入相关函数
count = int(input('Input time :'))
num = int(input('Input number :'))          # 由用户输入运算次数与开始数字
median = 0
lit = []

for str in range(count) :
    median = num + median                   #
    num = num*10                            # 升位
    lit.append(median)
    #print(lit[-1],'1 test')

def add(a,b):
    return a+b

print('Result :',reduce(add,(lit)),'2 test')
# reduce() 函数会对参数序列中元素进行累积。reduce(function, iterable[, initializer])
