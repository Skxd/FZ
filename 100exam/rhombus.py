# 100exam 23 屏幕上输出菱形
rho = int(input('Input :'))                 # 根据用户输入数字，输出不同行数菱形
rr = rho % 2           # tt,rr为‘ ’，‘*’号输出数量用
tt = rho // 2
if rho%2!=0 :                               # 输入的是奇数
    for result in range(1,rho+1) :
        if result+1 <= rho//2+1 :               # ‘rho//2+1’输出上一半
            print(' '*tt,'*'*rr)
            #print(tt,rr,'if')                  # 过程中测试用
            tt -= 1
            rr += 2
        else:                                   # 另一半
            print(' ' * tt, '*' * rr)
            #print(tt, rr)
            tt += 1
            rr -= 2
else:                                       # 输入的是偶数
    for result in range(1, rho + 2):
        if result+1 <= rho//2+1 :               # ‘rho//2+1’输出上一半
            print('',' '*(tt-1),'/'*(rr+1))
            #print(tt,rr,'if')
            tt -= 1
            rr += 2
        else:                                   # 另一半
            print(' ' * tt, '/' * (rr+1))
            #print(tt, rr)
            tt += 1
            rr -= 2
