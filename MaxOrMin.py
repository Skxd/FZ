#A = int(input('输入十进制数字 :'))
#print('相应十六进制',hex(A))
# 取出列表中最大最小值

mi = 0
A = [88,36,86,91,1,128,23,99,-1,52,66,38,-12,-6,87,41]
for x in A :
    if x < mi :
        mi = x
    else:
        x = mi
print(mi)#最小值
for x in A :
    if x > mi :
        mi = x
    else:
        x = mi
print(x)#最大值
