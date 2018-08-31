a = input()                                 # 判断一个数字是否是水仙花数
tu = []
for x in range(len(a)) :
    for b in a[x] :
        print(b)
        tu.append(b)
        for ttuu in tu :
            pass
print(int(tu[0]) * int(tu[1]))
