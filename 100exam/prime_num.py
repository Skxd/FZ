import time
low = int(input('input lower limit :'))                         # 用户输入上下限
up = int(input('input upper limit :'))
count = 0                                                       # 计数器，累加素数个数
dict = {}
for val in range(low,up) :                                      # 从下限值开始循环
    for divisor in range(2,val):                                # 从 2 到下限作为除数计算
        if val % divisor == 0 :                                 # 除法计算值为 0 ，即区间内存在其它因数，不是素数结束循环
            break
    else:
        count += 1
        print('This',count,'th prime number. ','is :',val)
        dict[count] = val
#print(dict)
print('运行时间:',time.perf_counter())
