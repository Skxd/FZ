b = 0
for b in range(1,10):                               # 循环分别输出两个因数
    for a in range(1,10):
        print('%s*%s='%(a,b),a*b,'\t',end='')       # 计算结果
        if a == b :
            print('')                               # 换行，行向看乘法口诀表每行最后一项的因数相同
            break





