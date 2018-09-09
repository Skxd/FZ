# 100exam 30 判断回数
strr = input('Input Str : ')                            # 获取字符串
for i in range(1,len(strr)+1) :                         # 以字符串长度进行循环
    if strr[i-1] == strr[-i] :
        if len(strr)//2 ==len(strr)//2 :
            print('是回数哦~~')
            break
    else:
        print('这不是回数')
        break

a = input("输入一串数字: ")
b = a[::-1]                                     # 没搞懂[]里的参数
if a == b:
    print("%s 是回文"% a)
else:
    print("%s 不是回文"% a)