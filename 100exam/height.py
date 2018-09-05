# 100exam 20 一球从100米高度自由落下，每次落地后反跳回原高度的一半，求它在第10次落地时，共经过多少米？第10次反弹多高？
import time
height = int(input('Input height  :'))
count = int(input('Input time  :'))             # 设置初始高度和反弹次数
hei = height
height_list = []

for co in range(1,count+1) :
    if count == 1 :                                # 如果次数是 1 ，高返回设置高度
        height_list.append(height)
        print('经过总路程  ：',height)
    else:
        height_list.append(height)
        hei = hei/2                             # 下一次的回弹高度为上次一半
        time_height = hei                       # 第 co 次的高度
        height = height + hei*2                 # 总经过路程
print('经过总路程  ：',height)
print('每次回弹时经过的路程 ：',height_list)
print(time_height)
print('运行时间:',time.perf_counter())