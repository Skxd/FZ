# 100exam 27 将所输入的5个字符，以相反顺序打印出来
                                                        # 未使用递归
strr = input('Input Str : ')                            # 获取字符串
for i in range(1,len(strr)+1) :                         # 以字符串长度进行循环
    for anw in strr[-i] :                                   # 使用 [-i] 从字符串末尾获取字符
        print(anw,end='')                                   # 输出获取字符