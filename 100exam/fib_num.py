a = 0 # fib初始值
b = 1
while a < 100 :
    a,b = b,a+b                              # 赋值中，是 a=b(1)，b=a+b(0+1)，无先后顺序并行运算，故b!=a+b(1+1)
    print(a)                                 # 也因此 ‘ b,a = a+b,b ’,与上运算结果相同
