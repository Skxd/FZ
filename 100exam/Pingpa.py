# 100exam 22 甲队为a,b,c三人，乙队为x,y,z三人a说他不和x比，c说他不和x,z比
# 请编程序找出三队赛手的名单a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单
import time
for v1 in ['x','y','z'] :
    for v2 in ['x','y','z'] :
        for v3 in ['x','y','z'] :
            if v1 != v2 and v2 != v3 and v3 != v1 and v1 != 'x' and v3 != 'x' and v3 != 'z' :
                print('a和 %s 比赛，b和 %s 比赛 ,c和 %s 比赛'%(v1,v2,v3))
print(time.process_time())
print(time.perf_counter())